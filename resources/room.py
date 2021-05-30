from flask_restful import Resource, reqparse
from models.room import RoomModel


class Room(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=int,
        required=False,
        help="This field cannot be blank."
    )
    parser.add_argument('name',
        type=str,
        required=False,
        help="This field cannot be blank."
    )

    def post(self):
        data = Room.parser.parse_args()

        if data['name'] == "":
            return {"message": "A room name cant be blank"}, 400

        room = RoomModel(data['name'])
        room.save_to_db()

        return {"message": "Room created successfully."}, 201

    def get(self):
        return {'rooms': [{'id': x.id, 'name': x.name} for x in RoomModel.query.all()]}



    def delete(self):
        data = Room.parser.parse_args()
        room = RoomModel.find_by_id(data['id'])
        if room:
            room.delete_from_db()

        return {'message': 'Room deleted'}


