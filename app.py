from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Make sure to keep this secret and safe

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the ToDo
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_email = db.Column(db.String(100), nullable=False)  # Added user_email

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# Utility to check if a user exists
def user_exists(email, password=None):
    if not os.path.exists("users.txt"):
        return False
    with open("users.txt", "r") as f:
        users = [line.strip().split(",") for line in f.readlines()]
    for user in users:
        if email == user[0] and (password is None or password == user[1]):
            return True
    return False

# Signup route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if user_exists(email):
            return "User already exists. Try logging in."
        with open("users.txt", "a") as f:
            f.write(f"{email},{password}\n")
        return redirect("/login")
    return render_template("signup.html")

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if user_exists(email, password):
            session["user"] = email
            return redirect("/")  # Redirect to the home page after successful login
        return "Invalid credentials. Try again."
    return render_template("login.html")

# Logout route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

# Home route (Dashboard)
@app.route("/", methods=["GET", "POST"])
def hello_world():
    if "user" not in session:
        return redirect("/login")
    user_email = session["user"]

    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc, user_email=user_email)  # Save with user email
        db.session.add(todo)
        db.session.commit()

    # Show only ToDos related to the logged-in user
    allTodo = Todo.query.filter_by(user_email=user_email).all()  # Filter ToDos by user email
    return render_template("index.html", allTodo=allTodo)

# Update ToDo route
@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    if "user" not in session:
        return redirect("/login")
    user_email = session["user"]
    todo = Todo.query.filter_by(sno=sno, user_email=user_email).first()  # Check user email in ToDo
    if not todo:
        return "Todo not found or you don't have permission to edit it."
    
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo.title = title
        todo.desc = desc
        db.session.commit()
        return redirect("/")
    return render_template("update.html", todo=todo)

# Delete ToDo route
@app.route("/delete/<int:sno>")
def delete(sno):
    if "user" not in session:
        return redirect("/login")
    user_email = session["user"]
    todo = Todo.query.filter_by(sno=sno, user_email=user_email).first()  # Check user email in ToDo
    if not todo:
        return "Todo not found or you don't have permission to delete it."
    
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
