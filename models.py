# from app import db  # Import db from app.py
from extensions import db

class User(db.Model):
    """ User model """
    __tablename__ = "users_line"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    # db.create_all()