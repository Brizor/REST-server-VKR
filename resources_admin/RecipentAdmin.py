from flask_restful import Resource, reqparse
from models.recipent import RecipentModel

class RecipentAdmin(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('id',
                        type=int,
                        required=False,
                        help="This field cannot be blank."
                        )
    parser.add_argument('user_id',
        type=int,
        required=False,
        help="This field cannot be blank."
    )
    parser.add_argument('room_id',
        type=int,
        required=False,
        help="This field cannot be blank."
    )


    def get(self):
        data = []
        for item in RecipentModel.find_all():
            data.append({
                "id":item.id,
                "user_id": item.user_id,
                "room_id": item.room_id})
        return data

    def post(self):
        data = RecipentAdmin.parser.parse_args()

        recipent = RecipentModel(data['user_id'], data['room_id'])
        recipent.save_to_db()

        return {"message": "Recipent created successfully."}, 201

    def delete(self):
        data = RecipentAdmin.parser.parse_args()
        recipent = RecipentModel.find_by_id(data['id'])
        if recipent:
            recipent.delete_from_db()
        return {"message": "Recipent deleted successfully."}, 200

    def put(self):
        data = RecipentAdmin.parser.parse_args()
        print(data)
        recipent = RecipentModel.find_by_id(data["id"])

        if recipent is None:
            recipent = RecipentModel(data['user_id'], data['room_id'])
        else:
            recipent.user_id = data['user_id']
            recipent.room_id = data['room_id']

        recipent.save_to_db()

        return {"message": "Recipent updated successfully."}, 200