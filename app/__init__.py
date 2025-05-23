from flask import Flask
from app.db import init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
app.config['DATABASE'] = 'todo.db'

init_db(app)

from app import routes  # noqa: F401, E402
