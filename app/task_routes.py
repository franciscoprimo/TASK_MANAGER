from flask import render_template, request, redirect, url_for, jsonify, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app import db
from app.models import User
from .crud import add_task, get_tasks, update_task, delete_task

# Blueprint para as rotas de tarefas
task_routes = Blueprint("task_routes", __name__, url_prefix="/")

# Redireciona "/" para a tela de login
@task_routes.route('/')
def home():
    return redirect(url_for('task_routes.login'))  # A página inicial agora é a tela de login

# Rota para login
@task_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = True if request.form.get('remember') else False  # Adiciona a opção "Lembrar-me"

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):  # Comparação segura de senha
            login_user(user, remember=remember)  # Agora o usuário pode ser lembrado
            return redirect(url_for('task_routes.dashboard'))  # Vai para o Dashboard após login
        else:
            return 'Falha no login. Tente novamente.'

    return render_template('login.html')

# Rota para logout
@task_routes.route('/logout')
@login_required  # Evita que usuários deslogados acessem essa rota
def logout():
    logout_user()
    return redirect(url_for('task_routes.login'))  # Redireciona para login após logout

# Rota para o Dashboard (acessível apenas para usuários logados)
@task_routes.route('/dashboard')
@login_required  # Somente usuários logados podem acessar
def dashboard():
    return render_template('dashboard.html')

# Rota para cadastro de usuário (Signup)
@task_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verifica se o usuário já existe
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "Nome de usuário já existe. Escolha outro."

        # Criptografa a senha antes de salvar
        hashed_password = generate_password_hash(password)

        # Cria um novo usuário no banco
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('task_routes.login'))  # Redireciona para login após cadastro

    return render_template('singup.html')  # Exibe a página de cadastro (arquivo "singup.html")

# CRUD de Tarefas (Apenas para usuários logados)
@task_routes.route('/tasks', methods=['POST'])
@login_required
def create_task():
    task_data = request.get_json()
    task_id = add_task(task_data['task_name'], task_data['description'], task_data.get('done', False))
    return jsonify({"message": "Tarefa adicionada com sucesso!", "id": task_id}), 201

@task_routes.route('/tasks', methods=['GET'])
@login_required
def list_tasks():
    tasks = get_tasks()
    return jsonify(tasks), 200

@task_routes.route('/tasks/<int:task_id>', methods=['PUT'])
@login_required
def update_task_route(task_id):
    task_data = request.get_json()
    updated = update_task(task_id, task_data['task_name'], task_data['description'], task_data.get('done', False))
    if updated:
        return jsonify({"message": "Tarefa atualizada com sucesso!"}), 200
    else:
        return jsonify({"error": "Tarefa não encontrada!"}), 404

@task_routes.route('/tasks/<int:task_id>', methods=['DELETE'])
@login_required
def delete_task_route(task_id):
    deleted = delete_task(task_id)
    if deleted:
        return jsonify({"message": "Tarefa deletada com sucesso!"}), 200
    else:
        return jsonify({"error": "Tarefa não encontrada!"}), 404