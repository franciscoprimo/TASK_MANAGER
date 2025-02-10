from app import create_app

app = create_app()

# Rodando a aplicação Flask no host 0.0.0.0 e porta 5000
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)