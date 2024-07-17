# app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message="Hello, World!")

@app.route('/api/data')
def get_data():
    data = {
        "items": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"}
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

# Procfile
web: gunicorn app:app

# requirements.txt
Flask==2.0.1
gunicorn==20.1.0