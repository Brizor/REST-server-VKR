import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class User(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=int,
        required=False,
        help="This field cannot be blank."
    )
    parser.add_argument('username',
        type=str,
        required=False,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=False,
        help="This field cannot be blank."
    )
    parser.add_argument('name',
        type=str,
        required=False,
        help="This field cannot be blank."
    )
    parser.add_argument('second_name',
        type=str,
        required=False,
        help="This field cannot be blank."
    )

    def get(self):

        data = User.parser.parse_args()
        room = UserModel.find_by_id(data['id'])
        if room:
            return {'users': [{'id': x.id,
                               'username': x.username,
                               'password': x.password,
                               'name': x.name,
                               'second_name': x.second_name,
                               'is_active': x.is_active
                               } for x in UserModel.query.all()]}
        return {'message': 'User not found'}, 404


    def post(self):
        data = User.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], data['password'], data['name'], data['second_name'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201


    def delete(self):
        data = User.parser.parse_args()
        user = UserModel.find_by_id(data['id'])
        if user:
            user.delete_from_db()

        return {'message': 'User deleted'}



