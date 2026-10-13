import os
import json
import re
import threading
import uuid
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from supabase import create_client
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


def get_supabase():
    if not SUPABASE_URL or not SUPABASE_KEY:
        return None

    try:
        return create_client(SUPABASE_URL, SUPABASE_KEY)
    except Exception:
        return None


supabase = get_supabase()
USER_STORE_PATH = Path(__file__).with_name("users.json")
_user_store_lock = threading.Lock()


def read_users():
    if not USER_STORE_PATH.exists():
        return []

    with USER_STORE_PATH.open("r", encoding="utf-8") as store:
        payload = json.load(store)
    users = payload.get("users", [])
    return users if isinstance(users, list) else []


def write_users(users):
    temporary_path = USER_STORE_PATH.with_suffix(".json.tmp")
    with temporary_path.open("w", encoding="utf-8") as store:
        json.dump({"users": users}, store, indent=2)
        store.write("\n")
    os.replace(temporary_path, USER_STORE_PATH)


def public_user(user):
    return {
        "id": user["id"],
        "email": user["email"],
        "full_name": user["full_name"],
        "phone": user["phone"],
    }


@app.route("/")
def home():
    if supabase is None:
        return jsonify({
            "success": False,
            "message": "Supabase configuration is missing. Set SUPABASE_URL and SUPABASE_KEY in your environment."
        }), 500

    response = supabase.table("test_connection").select("*").execute()
    return {
        "message": "Supabase connection successful!",
        "data": response.data,
    }


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({
            "success": False,
            "message": "Request body must be a JSON object"
        }), 400

    email = str(data.get("email", "")).strip().lower()
    password = data.get("password", "")

    if not email or not isinstance(password, str) or not password:
        return jsonify({
            "success": False,
            "message": "Email and password are required"
        }), 400

    try:
        with _user_store_lock:
            user = next((item for item in read_users() if item.get("email") == email), None)
        if user is None or not check_password_hash(user["password_hash"], password):
            return jsonify({
                "success": False,
                "message": "Invalid email or password.",
            }), 401
        return jsonify({
            "success": True,
            "message": "Login successful",
            "user": public_user(user),
        })
    except (OSError, json.JSONDecodeError, KeyError):
        return jsonify({
            "success": False,
            "message": "Unable to read local account data.",
        }), 500


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"success": False, "message": "Request body must be a JSON object"}), 400

    full_name = str(data.get("full_name", "")).strip()
    email = str(data.get("email", "")).strip().lower()
    phone = str(data.get("phone", "")).strip()
    password = data.get("password", "")

    if not full_name or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        return jsonify({"success": False, "message": "Enter a name and valid email address."}), 400
    if not isinstance(password, str) or len(password) < 6:
        return jsonify({"success": False, "message": "Password must be at least 6 characters."}), 400

    user = {
        "id": str(uuid.uuid4()),
        "email": email,
        "full_name": full_name,
        "phone": phone,
        "password_hash": generate_password_hash(password),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }

    try:
        with _user_store_lock:
            users = read_users()
            if any(item.get("email") == email for item in users):
                return jsonify({"success": False, "message": "An account with this email already exists. Please log in."}), 409
            users.append(user)
            write_users(users)
    except (OSError, json.JSONDecodeError):
        return jsonify({"success": False, "message": "Unable to save the local account."}), 500

    return jsonify({"success": True, "user": public_user(user)}), 201


@app.route("/google-login", methods=["GET"])
def google_login():
    if supabase is None:
        return jsonify({
            "success": False,
            "message": "Supabase credentials are not configured"
        }), 500

    try:
        response = supabase.auth.sign_in_with_oauth({
            "provider": "google",
            "options": {
                "redirect_to": "http://localhost:3000",
            },
        })

        return jsonify({
            "success": True,
            "url": response.url,
        })

    except Exception as exc:
        return jsonify({
            "success": False,
            "message": str(exc),
        }), 500


if __name__ == "__main__":
    app.run(debug=False, port=5000)