import sqlite3
from flask_restful import reqparse,Resource
from db import db
class UserModel(db.Model):
    __tablename__ = 'users'
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password

    @classmethod
    def find_by_username(cls,username):
        connection=sqlite3.connect('test.db')
        cursor=connection.cursor()
        #print(username)

        query="SELECT * FROM users WHERE username=?"

        result=cursor.execute(query,(username,))

        row=result.fetchone()
        print(row)
        if row:
            user=cls(*row) #user=cls(*row) //passing data to constructor same as we do through user=User(row[0],row[1],row[2])
        else:


            user=None
        #connection.commit()
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(
                *row)  # user=cls(*row) //passing data to constructor same as we do through user=User(row[0],row[1],row[2])
        else:

            user = None
        #connection.commit()
        connection.close()
        return user