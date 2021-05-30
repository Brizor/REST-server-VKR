import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'Users'
    __table_args__ = (
        db.UniqueConstraint('username', 'password', name='unique_user_pas'),
    )

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.String(30), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)

    recipents = db.relationship('RecipentModel', backref='Users', lazy=True)
    message = db.relationship('MessageModel', backref='Users', lazy=True)

    def __init__(self, username, password, name, second_name, is_active=False):
        self.username = username
        self.password = password
        self.name = name
        self.second_name = second_name
        self.is_active = is_active

    def save_to_db(self):
        print(dir(db.session.connection));
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def authoriztion(cls, username, password):
        return cls.query.filter_by(username=username, password=password).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return  cls.query.all()