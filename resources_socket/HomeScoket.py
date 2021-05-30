import sqlite3
from flask_restful import Resource, reqparse
from models.recipent import RecipentModel
from models.room import RoomModel

class HomeSocket(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('user_id',
        type=int,
        required=True,
        help="This field cannot be blank."
    )


    def get(self):
        data = HomeSocket.parser.parse_args()
        print(data)
        print('home')

        rooms = []

        recipent_for_user = RecipentModel.find_all_rooms(data['user_id'])
        for recipent in recipent_for_user:
            room = RoomModel.find_by_id(recipent.room_id)
            rooms.append({"id": room.id, "name": room.name})
            print(recipent.room_id)
        print(rooms)
        return rooms






        return {'message': 'rooms not found'}, 404