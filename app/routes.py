from flask import render_template
from flask_login import login_required, current_user
from flask_socketio import send

from app import app, db, socketio
from app.models import ChatHistory, User

@app.route('/')
@login_required
def index():
    chats = ChatHistory.query.all()
    users = User.query.all()
    return render_template('index.html', chats=chats, users=users)

    
########## SOCKET CODE ##########

@socketio.on('connect')
def handle_connect():
    if current_user.is_authenticated:
        current_user.is_online = True
        db.session.commit()
        print('Client Connected - ', current_user.username)

@socketio.on('disconnect')
def handle_disconnect():
    if current_user.is_authenticated:
        current_user.is_online = False
        db.session.commit()
        print('Client disconnected - ', current_user.username)

@socketio.on('message')
def handle_message(msg):
    ch = ChatHistory(message=msg, author_id=current_user.id)
    db.session.add(ch)
    db.session.commit()
    send({
        'msg': msg,
        'author': current_user.username 
    }, broadcast=True)