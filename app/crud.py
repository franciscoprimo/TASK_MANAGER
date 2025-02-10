import psycopg2
from .database import create_connection

def add_task(task_name, description, done):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tasks (task_name, description, done)
            VALUES (%s, %s, %s) RETURNING id
        """, (task_name, description, done))
        task_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return task_id
    except Exception as e:
        print(f"Erro ao adicionar tarefa: {e}")
        return None

def get_tasks():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        cursor.close()
        conn.close()
        return tasks
    except Exception as e:
        print(f"Erro ao obter tarefas: {e}")
        return []

def update_task(task_id, task_name, description, done):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE tasks SET task_name = %s, description = %s, done = %s
            WHERE id = %s
        """, (task_name, description, done, task_id))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao atualizar tarefa: {e}")
        return False

def update_task_in_db(task_id, task_name, description, done):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        update_query = """
            UPDATE tasks
            SET task_name = %s, description = %s, done = %s
            WHERE id = %s
            RETURNING id
        """
        cursor.execute(update_query, (task_name, description, done, task_id))
        
        # Confirmando a transação
        updated_task_id = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return updated_task_id  # Retorna o ID da tarefa atualizada, ou None se não encontrar

    except Exception as e:
        print(f"Erro ao atualizar tarefa: {e}")
        return None
    
def delete_task(task_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Erro ao deletar tarefa: {e}")
        return False