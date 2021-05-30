from db import db


class RoomModel(db.Model):
    __tablename__ = 'Rooms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    recipents = db.relationship('RecipentModel', backref='Rooms', lazy=True)
    message = db.relationship('MessageModel', backref='Rooms', lazy=True)


    def __init__(self, name):
        self.name = name

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
    def find_all(cls):
        return  cls.query.all()


