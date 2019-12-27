import sqlite3
from db import db


class PetModel(db.Model):
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    breed = db.Column(db.Text)
    species = db.Column(db.Text)
    gender = db.Column(db.Boolean, default=True)
    age = db.Column(db.Integer)

    user = db.relationship('UserModel')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, description, breed, species, gender, age, user_id):
        self.name = name
        self.description = description
        self.breed = breed
        self.species = species
        self.gender = gender
        self.age = age
        self.user_id = user_id

    def json(self):
        return{
            "name": self.name,
            "description": self.description,
            "breed": self.breed,
            "species": self.species,
            "gender": self.gender,
            "age": self.age,
            "user_id": self.user_id,
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, **data):
        self.name = data['name'] if data['name'] else self.name
        self.description = data['description'] if data['description'] else self.description
        self.breed = data['breed'] if data['breed'] else self.breed
        self.species = data['species'] if data['species'] else self.species
        self.gender = data['gender'] if data['gender'] else self.gender
        self.age = data['age'] if data['age'] else self.age
        self.user_id = data['user_id'] if data['user_id'] else self.user_id
