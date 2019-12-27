import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.user import UserModel
import sys


class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    @jwt_required()
    def get(self):
        uid = current_identity
        print(current_identity, file=sys.stderr)
        user = UserModel.find_by_id(uid.id)
        return {
            "id": user.id,
            "username": user.username,
        }

    def post(self):
        data = UserResource.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': "This user already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User created"}, 201
