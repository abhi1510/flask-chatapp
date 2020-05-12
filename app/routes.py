from flask import render_template
from flask_socketio import send

from app import app, db, socketio
from app.models import ChatHistory

@app.route('/')
def index():
    chats = ChatHistory.query.all()
    return render_template('index.html', chats=chats)

    
########## SOCKET CODE ##########

@socketio.on('message')
def handle_message(msg):
    ch = ChatHistory(message=msg)
    db.session.add(ch)
    db.session.commit()
    send(msg, broadcast=True)