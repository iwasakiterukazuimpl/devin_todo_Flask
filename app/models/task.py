from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    deadline = db.Column(db.Date, nullable=True)
    completed = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'

    @staticmethod
    def get_all():
        return Task.query.order_by(Task.id.desc()).all()

    @staticmethod
    def create(title, description=None, deadline=None):
        task = Task(
            title=title,
            description=description,
            deadline=deadline,
            completed=False
        )
        db.session.add(task)
        db.session.commit()
        return task

    @staticmethod
    def get(id):
        return Task.query.get(id)

    @staticmethod
    def update(id, title, description=None, deadline=None, completed=False):
        task = Task.query.get(id)
        if task:
            task.title = title
            task.description = description
            task.deadline = deadline
            task.completed = completed
            db.session.commit()
        return task

    @staticmethod
    def delete(id):
        task = Task.query.get(id)
        if task:
            db.session.delete(task)
            db.session.commit()
        return task
