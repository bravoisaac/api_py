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
product_collection =db["produc"]

@app.route("/api/v1/products", methods=["POST"])
def create_product():
    new_product = request.get_json()
    product_collection.insert_one(new_product)
    return jsonify({"status": "Producto creado con éxito"})


@app.route("/api/v1/productsAll", methods=["GET"])
def get_all_products():
    products = product_collection.find()
    data = [product for product in products]
    for product in data:
        product["_id"] = str(product["_id"])
    return jsonify(data)


@app.route("/api/v1/product/<product_id>", methods=["GET"])
def get_product(product_id):
    product = product_collection.find_one({'_id': ObjectId(product_id)})
    if product:
        product["_id"] = str(product["_id"])
        return jsonify(product)
    return "", 404


@app.route("/api/v1/product/<product_id>", methods=["PUT"])
def update_product(product_id):
    updated_product = request.get_json()
    result = product_collection.update_one({'_id': ObjectId(product_id)}, {'$set': updated_product})
    if result.modified_count > 0:
        return jsonify({"status": "Producto actualizado con éxito"})
    return "", 404


@app.route("/api/v1/product/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    result = product_collection.delete_one({'_id': ObjectId(product_id)})
    if result.deleted_count > 0:
        return jsonify({"status": "Producto eliminado con éxito"}), 204
    return "", 404


if __name__ == '__main__':
    app.run(debug=True)