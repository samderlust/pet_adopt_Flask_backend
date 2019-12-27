import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from models.pet import PetModel
from flask import jsonify
import sys


class PetResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, location=["json"])
    parser.add_argument('description', type=str)
    parser.add_argument('breed', type=str)
    parser.add_argument('species', type=str)
    parser.add_argument('gender', type=bool)
    parser.add_argument('age', type=int)
    parser.add_argument('user_id', type=int)

    @jwt_required()
    def get(self):
        data = PetResource.parser.parse_args()
        pet = PetModel.find_by_name(data['name'])
        if pet:
            return pet.json()
        return {"message": "Pet not found"}, 404

    def post(self):
        data = PetResource.parser.parse_args()
        pet = PetModel(**data)

        try:
            pet.save_to_db()
        except:
            return {"message": "Error during create"}, 500

        return pet.json(), 201

    def put(self):
        data = PetResource.parser.parse_args()

        pet = PetModel.find_by_name(data['name'])

        if pet is None:
            pet = PetModel(**data)
        else:
            pet.update(**data)

        pet.save_to_db()

        return pet.json(), 200
