from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Inicializando as extensões
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Carregar as configurações do arquivo config.py
    app.config.from_object('app.config.Config')   

    # Inicializando extensões
    db.init_app(app)
    login_manager.init_app(app)

    # Configuração do Flask-Login
    login_manager.login_view = "task_routes.login"  # Define a página de login padrão

    # Importar modelos e rotas
    from app.models import User  # Importando User para evitar erro de referência
    from app.task_routes import task_routes

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Flask-Login carrega usuários automaticamente

    app.register_blueprint(task_routes)

    return app