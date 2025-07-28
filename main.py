from flask import Flask
from serverless_http import create_handler

app = Flask(__name__)

@app.route('/')
def hello():
    return "Привет"

@app.route('/<path:path>')
def catch_all(path):
    return f"Маршрут /{path} не найден", 404

handler = create_handler(app)  # Создаём handler для Vercel
