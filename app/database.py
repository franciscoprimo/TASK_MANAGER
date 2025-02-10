import psycopg2
from psycopg2 import sql
from app import db
from app.models import User, Task
import os
conn = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST')
)

def create_db():
    # Criando as tabelas no banco de dados dentro do contexto da aplicação
    from app import create_app  # Importando a função create_app para o contexto
    app = create_app()
    
    with app.app_context():
        db.create_all()  # Agora o db.create_all() será chamado com o contexto da aplicação
        print("Tabelas criadas com sucesso!")