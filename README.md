# 🛒 Mohalla Mart
### Your Neighborhood. Your Market. Just a Click Away. 🌿

<p align="center">
  <b>A modern neighborhood grocery shopping platform designed to bring everyday essentials closer to your doorstep.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-Mohalla%20Mart-FF8A3D?style=for-the-badge&logo=shopify&logoColor=white" alt="Mohalla Mart"/>
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JavaScript-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="Frontend"/>
  <img src="https://img.shields.io/badge/Backend-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Auth-Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase"/>
</p>

---

## 🌟 About the Project

**Mohalla Mart** is a neighborhood-focused grocery shopping platform built to make everyday shopping simple, convenient, and accessible.

From fresh produce to household essentials, the platform aims to provide a smooth shopping experience with an intuitive interface, user authentication, cart management, and a personalized shopping journey.

The idea is simple: **bring the convenience of online grocery shopping to the heart of every neighborhood.**

## ✨ Features

| Feature | Description |
|---|---|
| 🛍️ Product Browsing | Explore everyday groceries and household essentials. |
| 🔎 Product Search | Find products quickly and conveniently. |
| 🛒 Shopping Cart | Add products and manage your shopping selections. |
| 🔐 Authentication | Support for account access and Google sign-in through Supabase. |
| 👤 Personalized Experience | Display a personalized shopping interface after login. |
| 🎁 Shopping Offers | Showcase promotional offers and eligible free gifts. |
| 📱 Responsive Interface | Designed with a clean, user-friendly shopping experience in mind. |
| ⚡ Interactive UI | Dynamic interactions for browsing and shopping. |

*Features may vary depending on the current implementation and deployment.*

## 🎨 Design Philosophy

Mohalla Mart uses a friendly, neighborhood-inspired visual identity.

- 🤍 **Clean interface:** A simple, uncluttered shopping experience.
- 🟠 **Warm accents:** Orange highlights for important actions and offers.
- 🌿 **Fresh identity:** Green accents inspired by groceries and freshness.
- 🧭 **Easy navigation:** Keep essential shopping actions accessible.

## 🧰 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask or the configured Python web framework

### Authentication and Database
- Supabase Authentication
- Supabase database services, where configured

### Development Tools
- Visual Studio Code
- Git and GitHub
- Local development server

## 🏗️ Architecture

```text
                 ┌────────────────────────┐
                 │       Customer         │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │     Mohalla Mart UI    │
                 │      HTML / CSS / JS   │
                 └───────────┬────────────┘
                             │
                 ┌───────────┴────────────┐
                 ▼                        ▼
       ┌──────────────────┐    ┌──────────────────┐
       │ Python Backend   │    │ Supabase Auth    │
       │ APIs and Logic   │    │ Google Sign-in   │
       └─────────┬────────┘    └──────────────────┘
                 │
                 ▼
       ┌──────────────────┐
       │ Database / Data  │
       └──────────────────┘
```

*This diagram represents the intended high-level structure. Adjust the database and service connections to match your actual implementation.*

## 🚀 Getting Started

### Prerequisites

Install the following tools:

- Python 3
- Node.js and npm, if using a Node-based local development server
- Visual Studio Code
- A Supabase project for authentication

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/mohalla-mart.git
cd mohalla-mart
```

Replace `YOUR_USERNAME` and the repository name with your actual GitHub details.

### 2. Start the frontend

If your project contains `Mohalla_Mart.html`, start a local server from the directory containing that file.

For example, using Node.js and a compatible static server:

```bash
npx serve .
```

Open the local URL displayed in your terminal and navigate to `Mohalla_Mart.html`.

Alternatively, if your existing project uses a different server, continue using its configured command.

### 3. Configure the Python backend

Navigate to the backend directory if your project has one:

```bash
cd backend
```

Create and activate a virtual environment.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

Install the dependencies listed in your project's `requirements.txt`:

```bash
pip install -r requirements.txt
```

Start the application using the entry point configured in your project. For example, if the file is `app.py`:

```bash
python app.py
```

### 4. Configure Supabase

1. Create or open your Supabase project.
2. Configure the authentication providers you intend to support.
3. Set the correct redirect URLs for local development and production.
4. Use the publishable key in the frontend only with appropriate database access policies.
5. Keep private keys, database passwords, and service-role credentials on the server.

Never commit secrets or real customer information to GitHub.

## 🔒 Security Considerations

Security is an essential part of a shopping platform.

- Validate user input on the backend.
- Enforce authorization for protected endpoints.
- Configure Row Level Security (RLS) on exposed Supabase tables.
- Protect customer profiles, addresses, and order information.
- Apply rate limiting to authentication and sensitive APIs.
- Use HTTPS in production.
- Calculate prices, discounts, and order totals on the server.
- Store secrets in environment variables or a secure secrets manager.
- Test authentication and authorization before deployment.

## 🗺️ Roadmap

Potential future enhancements include:

- [ ] Product categories and advanced filters
- [ ] Live inventory and stock management
- [ ] Order history and order tracking
- [ ] Secure online payment integration
- [ ] Delivery status notifications
- [ ] Personalized product recommendations
- [ ] Admin dashboard and analytics
- [ ] Progressive Web App (PWA) support
- [ ] Accessibility improvements
- [ ] Automated testing and CI/CD

## 📸 Screenshots

Add screenshots of your actual application to a `screenshots/` directory.

For example:

```text
screenshots/
├── homepage.png
├── login.png
├── create-account.png
└── cart.png
```

Then display them in this section:

```markdown
![Mohalla Mart Homepage](screenshots/homepage.png)
```

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your implementation.
5. Submit a pull request describing your improvements.

## 🎯 Project Goal

Mohalla Mart aims to make neighborhood shopping more convenient through an accessible digital experience that connects everyday shopping needs with technology.

## 👨‍💻 Developer

**Abhishek K**

Artificial Intelligence & Machine Learning  
CMR Institute of Technology, Bengaluru

---

<p align="center">
  <b>Made with ❤️ for every neighborhood.</b>
  <br/>
  🌿 Mohalla Mart — Your Neighborhood. Your Market. Just a Click Away.
</p>
