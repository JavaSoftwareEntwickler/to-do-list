# routes.py
from flask import Blueprint, Flask, render_template, request, redirect
from .models import db, Task

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

main = Blueprint('main', __name__)  # qui definisci 'main'!

@main.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['POST'])
def add_task():
    new_task = Task(title=request.form['title'])
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

@main.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    task = Task.query.get(task_id)
    task.completed = not task.completed
    db.session.commit()
    return redirect('/')

