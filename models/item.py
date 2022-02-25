import sqlite3
from flask_restful import reqparse,Resource
from db import db

class ItemModel(db.Model):
    __tablename__='items'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    price = db.Column(db.Float)

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def json(self):
        return {'name':self.name,'price':self.price}


    @classmethod
    def search_item(cls, name):


        x=ItemModel.query.filter(ItemModel.name==name).first()
        return x




    def insert_item(self):



        db.session.add(self)
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()

