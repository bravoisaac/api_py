import hashlib
import datetime
from bson import ObjectId
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_jwt_extended import JWTManager, create_access_token


app = Flask(__name__)
jwt = JWTManager(app)


app.config['JWT_SECRET_KEY']= "DuocCode"
app.config['JWT_ACCESS_TOKEN_EXPIRES']=datetime.timedelta(days=1)


uri = "mongodb+srv://isbravo:ktLGzXsKDnufOr3g@cluster1.kabn980.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db =  client["demoUnab"]
Compra_collection =db["produc"]

@app.route("/api/v1/Compra", methods=["POST"])
def Compra_product():
    return 


@app.route("/api/v1/CompraAll", methods=["GET"])
def get_all_Compra():
    return 


@app.route("/api/v1/Compra/<Compra_id>", methods=["GET"])
def get_Compra(Compra_id):
    return "", 404


@app.route("/api/v1/Compra/<Compra_id>", methods=["PUT"])
def update_Compra(Compra_id):
    return "", 404


@app.route("/api/v1/Compra/<Compra_id>", methods=["DELETE"])
def delete_Compra(Compra_id):
    return "", 404


if __name__ == '__main__':
    app.run(debug=True)