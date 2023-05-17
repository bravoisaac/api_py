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
user_collection =db["users"]


@app.route("/api/v1/users", methods=["POST"])
def create_user():
    new_user= request.get_json()
    new_user["password"] =  hashlib.sha256(new_user["password"].encode("utf-8")).hexdigest()
    doc =  user_collection.find_one({"username" : new_user["username"]})
    if not doc:
         user_collection.insert_one(new_user)
         return jsonify({"status" : "Usuario creado con exito"})
    else:
         return jsonify({"status" : "Usuario ya existe"})


@app.route("/api/v1/login", methods=["POST"])
def login():
     login_details = request.get_json()
     user = user_collection.find_one({"username" : login_details["username"]})
     if user:
          enc_pass = hashlib .sha256(login_details['password'].encode("utf-8")).hexdigest()
          if enc_pass ==user["password"]:
               access_token= create_access_token(identity=user["username"])
               return jsonify(access_token= access_token),200

     return jsonify({'msg':'Credenciales incorrectas'}),401



@app.route("/api/v1/usersAll",methods=["GET"])
#@jwt_required()
def get_all_users():
     users = user_collection.find()
     data=[]
     for user in users:
          user["_id"] = str(user["_id"])
          data.append(user) 
     return jsonify(data)


@app.route("/api/v1/user/<user_id>",methods=["DELETE"])
#@jwt_required()
def delete(user_id):
   
          delete_user = user_collection.delete_one({'_id':ObjectId(user_id)})
          if delete_user.deleted_count>0:
               return jsonify({"status" : "Usuario eliminado con exito"}),204
          else:
               return "",404
  


if __name__ == '__main__':
     app.run(debug=True) 

