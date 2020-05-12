from flask import Flask, render_template
from flask_socketio import SocketIO, send

from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# Socket Logic

@socketio.on('message')
def handle_message(msg):
    send(msg, broadcast=True)