from ext import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.String(128), primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(10))
    login_count = db.Column(db.Integer, default=0)
    last_login_ip = db.Column(db.String(128), default='')
