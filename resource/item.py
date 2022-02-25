from flask_restful import Resource, reqparse,request
from flask_jwt import jwt_required
from models.item import ItemModel
import sqlite3

class Item_List(Resource):

    def get(self):

        return  {'items': [x.json() for x in ItemModel.query.all()]},201
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
        item=ItemModel.search_item(name)
        if item:
            item.delete()
        return {"message":"item deleted successfully"},201

    def put(self,name):
        data = Item.parser.parse_args()

        item=ItemModel.search_item(name)
        print(item)
        if item is None:
            try:
                item=ItemModel(name,data['price'])

            except:
                return {'Message':' an error occured while inserting an item'},500
        else:
            try:

                item.price=data['price']

            except:
                return {'Message': 'an error occured while updating an item'},500
        item.insert_item()
        return item.json()



