from flask import render_template, request, redirect, url_for
from datetime import datetime
from app import app
from app.models import Task


@app.route('/')
def index():
    tasks = Task.get_all()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    description = request.form.get('description', '')
    deadline_str = request.form.get('deadline', '')

    deadline = None
    if deadline_str:
        try:
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
        except ValueError:
            pass

    Task.create(title, description, deadline)
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    title = request.form['title']
    description = request.form.get('description', '')
    deadline_str = request.form.get('deadline', '')
    completed = 'completed' in request.form

    deadline = None
    if deadline_str:
        try:
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
        except ValueError:
            pass

    Task.update(id, title, description, deadline, completed)
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    Task.delete(id)
    return redirect(url_for('index'))
