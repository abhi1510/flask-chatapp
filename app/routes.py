from flask import render_template
from flask_login import login_required
from flask_socketio import send

from app import app, db, socketio
from app.models import ChatHistory

@app.route('/')
@login_required
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