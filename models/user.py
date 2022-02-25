import sqlite3
from flask_restful import reqparse,Resource
from db import db
class UserModel(db.Model):
    __tablename__ = 'users'
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self,username,password):

        self.username=username
        self.password=password

    @classmethod
    def find_by_username(cls,username):
        print(UserModel.username)
        x=UserModel.query.filter(UserModel.username==username).first()
        print(x)
        return x
    @classmethod
    def find_by_id(cls, _id):
        return UserModel.query.filter(UserModel.id == _id)