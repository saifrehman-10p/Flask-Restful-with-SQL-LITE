import sqlite3
from flask_restful import reqparse,Resource
from db import db

class ItemModel(db.Model):
    __tablename__='items'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Float)
    price = db.Column(db.String)

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def json(self):
        return {'name':self.name,'price':self.price}


    @classmethod
    def search_item(cls, name):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items where name =?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()


        if row:
            return cls(*row)

        connection.close()




    def insert_item(self):
        #data = ItemModel.parser.parse_args()
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()
        insert_into = " INSERT INTO items(name,price) VALUES(?,?)"
        cursor.execute(insert_into, (self.name, self.price,))
        connection.commit()
        connection.close()

    def update_item(self):
        #data = Item.parser.parse_args()
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE items SET price=? WHERE name = ?", (self.price, self.name,))
        connection.commit()
        connection.close()

