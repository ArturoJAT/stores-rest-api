from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import  UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList #tienen que estar importados los modelos para que sqlalchemy cree sus tablas

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://nqblnalypuvyak:507830d105a5d5a7ab50cca2d41910246c713660d70b1bef18a630f86142aa78@ec2-54-243-223-245.compute-1.amazonaws.com:5432/d8fefcilq4l05j'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)



jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')

api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
