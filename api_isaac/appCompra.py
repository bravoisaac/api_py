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
# Crea un nuevo cliente y conéctate al servidor
client = MongoClient(uri, server_api=ServerApi('1'))
db =  client["demoUnab"]
product_collection = db["produc"]
cliente_collection = db["users"]
order_collection = db["order"]


@app.route("/api/v1/orders", methods=["POST"])
def create_order():
    new_order = request.get_json()
    cliente_id = new_order.get("users_id")
    product_id = new_order.get("produc_id")
    
    # Verificar si el cliente existe
    cliente = cliente_collection.find_one({'_id': ObjectId(cliente_id)})
    if not cliente:
        return jsonify({"status": "Cliente no encontrado"}), 404
    
    # Verificar si el producto existe y tiene stock suficiente
    product = product_collection.find_one({'_id': ObjectId(product_id)})
    if not product:
        return jsonify({"status": "Producto no encontrado"}), 404
    if product["stock"] < new_order.get("quantity"):
        return jsonify({"status": "Stock insuficiente"}), 400
    
    # Reducir el stock del producto y crear el pedido
    product_collection.update_one(
        {'_id': ObjectId(product_id)},
        {'$inc': {'stock': -new_order.get("quantity")}}
    )
    new_order["cliente_id"] = ObjectId(cliente_id)
    new_order["product_id"] = ObjectId(product_id)
    order_collection.insert_one(new_order)
    
    return jsonify({"status": "Pedido creado con éxito"})
# Modificar una order por id
@app.route("/api/v1/order/<order_id>", methods=["PUT"])
def update_order(order_id):
    updated_order = request.get_json()
    cliente_id = updated_order.get("cliente_id")
    product_id = updated_order.get("product_id")
    
    # Verificar si el cliente existe
    cliente = cliente_collection.find_one({'_id': ObjectId(cliente_id)})
    if not cliente:
        return jsonify({"status": "Cliente no encontrado"}), 404
    
    # Verificar si el producto existe y tiene stock suficiente
    product = product_collection.find_one({'_id': ObjectId(product_id)})
    if not product:
        return jsonify({"status": "Producto no encontrado"}), 404
    if product["stock"] < updated_order.get("quantity"):
        return jsonify({"status": "Stock insuficiente"}), 400
    
    # Actualizar el pedido y ajustar el stock del producto
    product_collection.update_one(
        {'_id': ObjectId(product_id)},
        {'$inc': {'stock': -updated_order.get("quantity")}}
    )
    updated_order["cliente_id"] = ObjectId(cliente_id)
    updated_order["product_id"] = ObjectId(product_id)
    result = order_collection.update_one(
        {'_id': ObjectId(order_id)},
        {'$set': updated_order}
    )
    if result.modified_count > 0:
        return jsonify({"status": "Pedido actualizado con éxito"})
    return "", 404

# eliminar un pedido por id
@app.route("/api/v1/order/<order_id>", methods=["DELETE"])
def delete_order(order_id):
    result = order_collection.delete_one({'_id': ObjectId(order_id)})
    if result.deleted_count > 0:
        return jsonify({"status": "Pedido eliminado con éxito"}), 204
    return "", 404


if __name__ == '__main__':
    app.run(debug=True)

# como generar un pedido nesesitas el id del user y del produto con su stok
#{
#  "users_id": "6464037c0a4eb752b6c7c966",
#  "produc_id": "646aeebaeaae2aef3abb7c8e",
#  "quantity": 1
#}
