from flask import Flask
from flask_restful import Api,Resource
from flask_jwt import JWT
from security import authenticate,identity
from resource.user import user_signup
from resource.item import Item,Item_List

app= Flask(__name__)
app.secret_key='saif'
api=Api(app)

jwt= JWT(app,authenticate,identity) #/auth

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Item_List, '/item/')
api.add_resource(user_signup, '/usersignup')

@app.before_first_request
def create_table():
    db.create_all()
if __name__=='__main__':
    from  db import  db
    db.init_app(app)
    app.run(port=5002,debug=True)