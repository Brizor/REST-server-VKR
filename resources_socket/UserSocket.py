import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserSocket(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )


    def get(self):
        data = UserSocket.parser.parse_args()
        print(data)
        user = UserModel.authoriztion(data['username'], data['password'])

        if user:
            return {'user_id': user.id,
                    'username': user.name,
                    'userkey': 'userkey' + str(user.id)}

        return {'message': 'User not found'}, 404