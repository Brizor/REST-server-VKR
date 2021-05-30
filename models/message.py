import sqlite3
from db import db
import datetime


class MessageModel(db.Model):
    __tablename__ = 'Messages'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('Rooms.id'), nullable=False)


    def __init__(self, user_id, room_id, content, date):
        self.user_id = user_id
        self.room_id = room_id
        self.content = content
        self.date = date


    def json(self):
        return {'user_id': self.user_id,
                'room_id': self.room_id,
                'content': self.content,
                'date': self.date}

    def save_to_db(self):
        db.session.add(self)
        print(dir(db.session))
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_ten_in_interval(cls,_room_id):
        return cls.query.filter_by(room_id=_room_id).all()

    @classmethod
    def find_all(cls):
        return  cls.query.all()
