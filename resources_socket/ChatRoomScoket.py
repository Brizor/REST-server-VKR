import sqlite3
from flask_restful import Resource, reqparse
from models.message import MessageModel
from models.user import UserModel
import datetime
class ChatRoomSocket(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=int,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('user_id',
        type=int,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('room_id',
        type=int,
        required=False,
        help="This field cannot be left blank!"
    )
    parser.add_argument('content',
                        type=str,
                        required=False,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        print('asdasdas')
        data = ChatRoomSocket.parser.parse_args()
        currentDate = datetime.datetime.today()
        message = MessageModel(data['user_id'], data['room_id'], data['content'], currentDate)

        print(message.date)
        message.save_to_db()
        return {"user_id": data['user_id'],
                "room_id": data['room_id'],
                "content": data['content'],
                "date": str(currentDate)[0:19]}, 404

    def get(self):
        data = ChatRoomSocket.parser.parse_args()
        messages = MessageModel.find_ten_in_interval(data['room_id'])


        listMessage = []
        for message in messages:
            listMessage.append({
                "content": message.content,
                "date": str(message.date)[0:19],
                "username": UserModel.find_by_id(message.user_id).username,
                "user_id": message.user_id,
                "room_id": message.room_id
            })
        print(listMessage)

        return listMessage

