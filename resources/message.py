from flask_restful import Resource, reqparse
from models.message import MessageModel
from datetime import date


class Message(Resource):
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
        data = Message.parser.parse_args()



        message = MessageModel(data['user_id'], data['room_id'], data['content'])
        message.save_to_db()

        return {"message": "message created successfully."}, 201

    def get(self):
        return {'messages': [{'id': x.id, 'user_id': x.user_id, 'room_id': x.room_id, 'content': x.content,'date': str(x.date)[0:16]} for x in MessageModel.query.all()]}



    def delete(self):
        data = Message.parser.parse_args()
        message = MessageModel.find_by_id(data['id'])
        if message:
            message.delete_from_db()

        return {'message': 'message deleted'}


class ItemList(Resource):
    def get(self):
        return {'messages': [x.json() for x in MessageModel.query.all()]}
