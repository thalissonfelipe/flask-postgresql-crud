from database.db import db
from datetime import datetime


class TimestampMixin:
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(TimestampMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.relationship(
        'Address', uselist=False, backref='users', cascade='all, delete')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "User(name='{}', age={}, address={})".format(
            self.name,
            self.age,
            self.address
        )

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'address': {
                'street': self.address.street,
                'number': self.address.number,
                'city': self.address.city,
                'state': self.address.state
            }
        }

    @classmethod
    def from_json(cls, json):
        return cls(json['name'], json['age'])


class Address(TimestampMixin, db.Model):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String, nullable=False)
    number = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)

    def __init__(self, street, number, city, state, user_id):
        self.street = street
        self.number = number
        self.city = city
        self.state = state
        self.user_id = user_id

    def __repr__(self):
        return "Address(street='{}', number={}, city='{}', state='{}')".format(
            self.street,
            self.number,
            self.city,
            self.state
        )

    def serialize(self):
        return {
            'id': self.id,
            'street': self.street,
            'number': self.number,
            'city': self.city,
            'state': self.state
        }

    @classmethod
    def from_json(cls, json, user_id):
        return cls(
            json['street'],
            json['number'],
            json['city'],
            json['state'],
            user_id
        )
