from app.db import get_db


class Todo:
    @staticmethod
    def get_all():
        db = get_db()
        todos = db.execute(
            'SELECT id, title, description, completed FROM todo '
            'ORDER BY id DESC'
        ).fetchall()
        return todos

    @staticmethod
    def create(title, description):
        db = get_db()
        db.execute(
            'INSERT INTO todo (title, description, completed) '
            'VALUES (?, ?, ?)',
            (title, description, False)
        )
        db.commit()

    @staticmethod
    def get(id):
        db = get_db()
        todo = db.execute(
            'SELECT id, title, description, completed FROM todo WHERE id = ?',
            (id,)
        ).fetchone()
        return todo

    @staticmethod
    def update(id, title, description, completed):
        db = get_db()
        db.execute(
            'UPDATE todo SET title = ?, description = ?, completed = ? '
            'WHERE id = ?',
            (title, description, completed, id)
        )
        db.commit()

    @staticmethod
    def delete(id):
        db = get_db()
        db.execute('DELETE FROM todo WHERE id = ?', (id,))
        db.commit()
