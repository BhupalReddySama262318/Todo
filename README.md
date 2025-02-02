# Flask ToDo Application

A secure and user-friendly ToDo application built with Flask that helps users manage their daily tasks efficiently with email-based authentication and a clean, responsive interface.

## 🚀 Live Demo
[View Live Demo](https://todo-lx12.onrender.com/login)

## ✨ Features
- User Authentication with Email
- Create, Read, Update, and Delete ToDos
- User-specific ToDo lists
- Responsive Bootstrap UI
- Real-time task management
- Secure data handling
- Cross-browser compatibility

## 🛠️ Technologies Used
- Backend:
  - Flask 3.1.0
  - Flask-SQLAlchemy 3.1.1
  - SQLite Database
- Frontend:
  - Bootstrap 5.3
  - Font Awesome 6.0
  - HTML5/CSS3

## 🚦 Getting Started
### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation
bash
Clone the repository
git clone https://github.com/yourusername/flask-todo-app.git
cd flask-todo-app
Create and activate virtual environment
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
Install dependencies
pip install -r requirements.txt
Initialize database
python
>>> from app import db
>>> db.create_all()
>>> exit()
Start application
python app.py

## 📖 Usage
1. Access the application at `http://localhost:5000`
2. Register with your email and password
3. Login to access your personal ToDo dashboard
4. Manage your tasks:
   - Add new tasks with title and description
   - View all tasks in organized table
   - Update existing tasks
   - Delete completed tasks
   - Track creation time of tasks

## 📁 Project Structure
```
flask-todo-app/
│
├── app.py                # Main Flask application
├── todo.db              # SQLite database
├── users.txt            # User credentials
├── requirements.txt     # Dependencies
├── Procfile            # Deployment config
│
└── templates/          
    ├── base.html       # Base template
    ├── index.html      # Dashboard
    ├── login.html      # Login page
    ├── signup.html     # Registration
    ├── update.html     # Todo update
    └── about.html      # About page
```

## 🔒 Security Features
- Email-based authentication
- Session management
- User-specific data isolation
- Password protection
- CSRF protection

## 🚀 Deployment
Currently deployed on Render:
1. Connect GitHub repository
2. Configure environment variables
3. Set up build command
4. Deploy with Gunicorn

## 💡 Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 📝 License
This project is licensed under the MIT License.

## 📫 Support & Contact
- GitHub Issues: Report bugs and feature requests
- Email: bhupalreddysama18@gmail.com
- Project Link: [https://github.com/BhupalReddySama262318/Todo.git](https://github.com/BhupalReddySama262318/Todo.git)

## 👏 Acknowledgments
- Flask Documentation
- Bootstrap Team
- SQLAlchemy Documentation
- Font Awesome Icons