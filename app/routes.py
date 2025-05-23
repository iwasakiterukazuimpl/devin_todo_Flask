from flask import render_template, request, redirect, url_for
from app import app
from app.models import Todo


@app.route('/')
def index():
    todos = Todo.get_all()
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    description = request.form['description']
    Todo.create(title, description)
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    title = request.form['title']
    description = request.form['description']
    completed = 'completed' in request.form
    Todo.update(id, title, description, completed)
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete(id):
    Todo.delete(id)
    return redirect(url_for('index'))
