import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel
from db import db


class user_signup(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This fileld cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This fileld cannot be left blank')
    def post(self):
        data = user_signup.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message":"user already exist"},400
        user1=UserModel(data['username'],data['password'])
        db.session.add(user1)
        db.session.commit()
        return {"message":"user added successfully"},201


