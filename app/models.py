from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Task(db.Model):
    _tablename_ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    done = db.Column(db.Boolean, default=False)

    def _init_(self, task_name, description, done=False):
        self.task_name = task_name
        self.description = description
        self.done = done

class User(db.Model, UserMixin):
    _tablename_ = 'users'  # Corrigido nome da tabela (antes estava com um erro "tablename")

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def _init_(self, username, password):
        self.username = username
        self.password = password