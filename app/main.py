from flask import Flask, render_template
from app import create_app

app = create_app()

@app.route('/')
def index():
    # Renderiza o template index.html na rota principal
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)