from flask_restful import Resource, reqparse
from models.room import RoomModel

class RoomAdmin(Resource):

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

    def get(self):
        data = []
        for item in RoomModel.find_all():
            data.append({
                "id": item.id,
                "name": item.name})
        return data

    def post(self):
        data = RoomAdmin.parser.parse_args()

        user = RoomModel(data['name'])
        user.save_to_db()

        return {"message": "Room created successfully."}, 201

    def delete(self):
        data = RoomAdmin.parser.parse_args()
        user = RoomModel.find_by_id(data['id'])
        if user:
            user.delete_from_db()
        return {"message": "Room deleted successfully."}, 200

    def put(self):
        data = RoomAdmin.parser.parse_args()
        print(data)
        room = RoomModel.find_by_id(data["id"])
        print(room)
        if room is None:
            room = RoomModel(data['name'])
        else:
            room.name = data['name']

        room.save_to_db()

        return {"message": "Room updated successfully."}, 200