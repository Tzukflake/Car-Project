from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

#skapar mina två tables för min databas samt skapar enrelationship mellan de två
class User(db.Model):
    __tablename__='users'
    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String)
    last_name = db.Column(String)
    personal_number = db.Column(String)
    address = db.Column(String)
    cars = db.relationship("Car", back_populates="owner")

class Car(db.Model):
    __tablename__="cars"
    id = db.Column(Integer, primary_key=True)
    brand = db.Column(String)
    model_name = db.Column(String)
    model_year = db.Column(String)
    color = db.Column(String)
    registration_plate= db.Column(String)
    owner_id = db.Column(Integer, ForeignKey('users.id'))
    owner = db.relationship('User', back_populates='cars')
