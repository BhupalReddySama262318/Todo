# Flask ToDo Application

A secure and user-friendly ToDo application built with Flask, featuring user authentication and persistent storage. This application allows users to manage their daily tasks efficiently with a clean and responsive interface.

## 🚀 Live Demo
[View Live Demo](https://your-deployed-app-url.herokuapp.com)

## ✨ Key Features
- User Authentication (Signup/Login)
- Create, Read, Update, and Delete ToDos
- User-specific ToDo lists
- Responsive Bootstrap UI
- Real-time updates
- Secure data handling
- Cross-browser compatibility

## 🛠️ Tech Stack
- Backend: Flask, SQLAlchemy, SQLite
- Frontend: Bootstrap 5.3, HTML/CSS, Font Awesome
- Deployment: Gunicorn
- Database: SQLite

## 🚦 Quick Start\

# Clone the repository

git clone https://github.com/yourusername/flask-todo-app.git

cd flask-todo-app


# Create and activate virtual environment

python -m venv venv

source venv/bin/activate # On Windows: venv\Scripts\activate


# Install dependencies

pip install -r requirements.txt


# Initialize database


python

>>> from app import db

>>> db.create_all()


>>> exit()

# Start application

python app.py

## 📖 Usage Guide
1. Access the application at `http://localhost:5000`
2. Register a new account at `/signup`
3. Login with your credentials
4. Add new ToDos using the form
5. Manage your ToDos:
   - View all tasks in the table
   - Update tasks using the edit button
   - Delete completed tasks
   - Mark tasks as complete
6. Logout when finished

## �� Project Structure



