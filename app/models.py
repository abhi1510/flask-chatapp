from app import db

class ChatHistory(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)