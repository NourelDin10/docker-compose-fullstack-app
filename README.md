# Docker Compose Full-Stack Application

## 📖 Overview

This repository provides a **containerized full-stack application** powered by Docker Compose. It demonstrates how to orchestrate a frontend, backend, and database in a development environment.

The stack includes:
- **Frontend:** Static website served by **Apache HTTPD**.
- **Backend:** A Flask API that connects to a MariaDB database.
-  **Database:** MariaDB, initialized with sample schema and data.

This setup is ideal for learning, prototyping, or bootstrapping small projects with Docker Compose.

---

## ✨ Features

- Containerized setup for easy deployment and development.
- Pre-configured database schema and seed data.
- Simple REST API to fetch users from the database.

---

## 📂 Project Structure

```bash
.
├── backend/                 # Flask backend application
│   ├── app.py               # Main Flask API
│   ├── Dockerfile           # Backend image definition
│   └── requirements.txt     # Python dependencies
├── frontend/                # Static frontend files (HTML, CSS, JS)
│    ├── index.html            
├── init/
│   └── init.sql             # Database schema & seed data
├── .env                     # Environment variables (configurable)
├── .gitignore
└── docker-compose.yml       # Compose file defining services
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/)  
- [Docker Compose](https://docs.docker.com/compose/)  

### Setup & Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/NourelDin10/docker-compose-fullstack-app.git
   cd docker-compose-fullstack-app
   ```

2. **Configure environment variables**  
   Update the `.env` file with your desired ports, database name, username, and password.

3. **Build and start the containers**
   ```bash
   docker-compose up --build
   ```

4. **Access the application**
   - **Frontend:** [http://localhost:8080](http://localhost:8080)  
   - **Backend API:** [http://localhost:5000](http://localhost:5000)

---

## 🔗 API Endpoints

| Method | Endpoint | Description            | Example Response |
|-------|----------|----------------------|----------------|
| GET   | `/`      | Returns list of users | `{ "users": ["Nour", "Ali"] }` |

---

## 🗄️ Database Details

- The database is initialized automatically from `init/init.sql`.  
- Default credentials are stored in `.env` (you can customize them).  

---

## 🛠️ Customization

- **Frontend:** Place your static HTML/CSS/JS files under `frontend/`.  
- **Backend:** Modify or extend the API logic in `backend/app.py`.  
- **Database:** Adjust schema and seed data in `init/init.sql` to fit your use case.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to **fork** the project and submit a **pull request**.
