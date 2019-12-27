from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_restful import Resource, reqparse

from db import db
from security import authenticate, identity
from resources.user import UserResource
from resources.pet import PetResource

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = "fkladsjfkladsfjl2312kjlj21l"
api = Api(app)


@app.before_first_request
def create_table():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(UserResource, '/register')
api.add_resource(PetResource, '/pet')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
