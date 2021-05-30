from flask_restful import Resource, reqparse
from models.message import MessageModel

class MessageAdmin(Resource):

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



    def get(self):
        data = []
        for item in MessageModel.find_all():
            data.append({
                "id":item.id,
                "content": item.content,
                "date": str(item.date)[0:19],
                "user_id": item.user_id,
                "room_id": item.room_id})
        return data


    def post(self):
        data = MessageModel.parser.parse_args()
        data = []


        return {"message": "User created successfully."}, 201

