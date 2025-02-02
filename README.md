# Flask ToDo Application

A secure and user-friendly ToDo application built with Flask, featuring user authentication and persistent storage. This application allows users to manage their daily tasks efficiently with a clean and responsive interface.

## 🚀 Live Demo
[View Live Demo](https://todo-lx12.onrender.com/login)

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

## 📁 Project Structure

flask-todo-app/
├── app.py # Main Flask application
├── todo.db # SQLite database
├── users.txt # User credentials
├── requirements.txt # Dependencies
├── Procfile # Deployment config
└── templates/ # HTML templates
├── base.html # Base template
├── index.html # Main dashboard
├── login.html # Login page
├── signup.html # Registration page
└── update.html # Todo update page

## 🔒 Security Features
- Session-based authentication
- User-specific data isolation
- Secure password handling
- CSRF protection

## 🚀 Deployment
Ready for deployment on platforms like Heroku:
1. Create a new Heroku app
2. Connect your GitHub repository
3. Deploy the main branch
4. Ensure environment variables are set
5. Launch the application

## 💡 Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 📝 License
This project is licensed under the MIT License.

## 📫 Support
- Report bugs: Open an issue
- Feature requests: Open an issue
- Questions: Open a discussion

## 👥 Contact
Your Name
- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)
- Project Link: [https://github.com/yourusername/flask-todo-app](https://github.com/yourusername/flask-todo-app)

## 🙏 Acknowledgments
- Flask Documentation
- Bootstrap Team
- SQLAlchemy Documentation
- Font Awesome Icons

