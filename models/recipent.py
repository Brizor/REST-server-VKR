import sqlite3
from db import db


class RecipentModel(db.Model):

    __tablename__ = 'Recipents'

    __table_args__ = (
        db.UniqueConstraint('user_id', 'room_id', name='unique_user_room'),
    )
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('Rooms.id'), nullable=False)

    def __init__(self, user_id, room_id):
        self.user_id = user_id
        self.room_id = room_id

    def json(self):
        return {'user_id': self.user_id,
                'room_id': self.room_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all_rooms(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def find_by_user_room(cls, user_id, room_id):
        return cls.query.filter_by(user_id=user_id, room_id=room_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
