import os
from flask import Flask
from flask_restful import Api
from resources.room import Room
from resources.user import User
from resources.recipent import Recipent,RecipentForSocket
from resources.message import Message

from resources_socket.UserSocket import UserSocket
from resources_socket.HomeScoket import HomeSocket
from resources_socket.ChatRoomScoket import ChatRoomSocket

from resources_admin.UserAdmin import UserAdmin
from resources_admin.RoomAdmin import RoomAdmin
from resources_admin.RecipentAdmin import RecipentAdmin
from resources_admin.MessageAdmin import MessageAdmin

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

api.add_resource(User, '/user')
api.add_resource(Room, '/room')
api.add_resource(Message, '/message')
api.add_resource(Recipent, '/recipent')

api.add_resource(UserSocket, '/authorization')
api.add_resource(HomeSocket, '/home')
api.add_resource(ChatRoomSocket, '/msgsocket')

api.add_resource(UserAdmin, "/useradmin")
api.add_resource(RoomAdmin, "/roomadmin")
api.add_resource(RecipentAdmin, "/recipentadmin")
api.add_resource(MessageAdmin, "/messageadmin")




if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5001)