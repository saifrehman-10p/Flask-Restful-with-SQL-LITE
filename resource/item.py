from flask_restful import Resource, reqparse,request
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3

class Item_List(Resource):

    def get(self):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)

        item=[]
        for i in result:
            item.append({'name':i[0],'price':i[1]})

        return  {'items': item},201
class Item(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('price', type=float, required=True, help='This fileld cannot be left blank')
    @jwt_required()
    def get(self,name):

        item=ItemModel.search_item(name)

        if item:

            return item.json()
        return {"message": "item doesnot exist"}




    def post(self, name):
        data = Item.parser.parse_args()
        item=ItemModel.search_item(name)

        if item:
            return {'Message ': 'Items Already Exsist'}, 400

        item=ItemModel(name,data['price'])
        try:

            item.insert_item()


        except:
            return {'message':'error occured while insering'}
        return item.json(), 201

    def delete(self, name):
        if not ItemModel.search_item(name):
            return {'Message ': 'Items doesnot Exsist'}, 400
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        cursor.execute("DELETE FROM items WHERE name = ?",(name,))
        connection.commit()
        connection.close()
        return {"message":"item deleted successfully"},201

    def put(self,name):
        data = Item.parser.parse_args()

        item=ItemModel.search_item(name)
        updateditem=ItemModel(name,data['price'])
        if item is None:
            try:
                updateditem.insert_item()

            except:
                return {'Message':' an error occured while inserting an item'},500
        else:
            try:
                updateditem.update_item()

            except:
                return {'Message': 'an error occured while updating an item'},500
        return updateditem.json()



