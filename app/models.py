from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_online = db.Column(db.Boolean, default=False)
    chats = db.relationship('ChatHistory',backref='author', lazy=True)

    def __repr__(self):
        return self.username

class ChatHistory(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)