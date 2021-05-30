from flask_restful import Resource, reqparse
from models.recipent import RecipentModel


class Recipent(Resource):

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

    def post(self):
        data = Recipent.parser.parse_args()

        if RecipentModel.find_by_user_room(data['user_id'], data['room_id']):
            return {"message": "A recipent exist"}, 400

        recipent = RecipentModel(data['user_id'], data['room_id'])
        recipent.save_to_db()

        return {"message": "recipent created successfully."}, 201

    def get(self):
        return {'recipents': [{'id': x.id, 'user_id': x.user_id, 'room_id': x.room_id} for x in RecipentModel.query.all()]}



    def delete(self):
        data = Recipent.parser.parse_args()
        recipent = RecipentModel.find_by_id(data['id'])
        if recipent:
            recipent.delete_from_db()

        return {'message': 'recipent deleted'}


class RecipentForSocket(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('user_id',
        type=int,
        required=True,
        help="This field cannot be blank."
    )


    def get(self):
        data = RecipentForSocket.parser.parse_args()
        print(data['user_id'])
        recipent = RecipentModel.find_all_rooms(data['user_id'])
        print(recipent)
        if recipent:
            return {'items': [x.json() for x in recipent]}
        return {'message': 'Store not found'}, 404

