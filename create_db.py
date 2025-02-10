import psycopg2

def create_connection():
    conn = psycopg2.connect(
        dbname="task_manager",
        user="task_user",
        password="senha",
        host="localhost"
    )
    return conn

def create_table():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id SERIAL PRIMARY KEY,
                task_name VARCHAR(255),
                description TEXT,
                done BOOLEAN
            )
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("Tabela 'tasks' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")

if __name__ == "__main__":
    create_table()