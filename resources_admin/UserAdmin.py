from flask_restful import Resource, reqparse
from models.user import UserModel

class UserAdmin(Resource):

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
        data = []
        for item in UserModel.find_all():
            data.append({
                "id":item.id,
                "username": item.username,
                "password": item.password,
                "name": item.name,
                "second_name": item.second_name})
        return data


    def post(self):
        data = UserAdmin.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], data['password'], data['name'], data['second_name'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201


    def delete(self):
        data = UserAdmin.parser.parse_args()
        user = UserModel.find_by_id(data['id'])
        if user:
            user.delete_from_db()
        return {"message": "User deleted successfully."}, 200

    def put(self):
        data = UserAdmin.parser.parse_args()
        print(data)
        user = UserModel.find_by_id(data["id"])
        print(user)
        if user is None:
            user = UserModel(data['username'], data['password'], data['name'], data['second_name'])


        else:
            user.username = data['username']
            user.password = data['password']
            user.name = data['name']
            user.second_name = data['second_name']
        user.save_to_db()

        return {"message": "User updated successfully."}, 200