import hashlib
import datetime
from bson import ObjectId
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_jwt_extended import JWTManager, create_access_token
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction




app = Flask(__name__)
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY']= "DuocCode"
app.config['JWT_ACCESS_TOKEN_EXPIRES']=datetime.timedelta(days=1)


# Configurar las credenciales de Transbank
commerce_code = 597055555532
api_key = '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C'
integration_type = 'TEST'  # Cambiar a 'LIVE' para producción

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

    # Crear una transacción en Webpay Plus
    transaction = Transaction.create(
        buy_order=new_order["order_id"],
        session_id=str(ObjectId()),
        amount=new_order["total_amount"],
        return_url=new_order["return_url"],
        commerce_code=commerce_code,
        api_key=api_key,
        integration_type=integration_type
    )

    try:
        # Obtener la URL de redireccionamiento a Webpay
        redirect_url = transaction.get_redirect_url()

        # Reducir el stock del producto y crear el pedido
        product_collection.update_one(
            {'_id': ObjectId(product_id)},
            {'$inc': {'stock': -new_order.get("quantity")}}
        )
        new_order["cliente_id"] = ObjectId(cliente_id)
        new_order["product_id"] = ObjectId(product_id)
        new_order["transaction_token"] = transaction.token
        order_collection.insert_one(new_order)

        return jsonify({
            "status": "Pedido creado con éxito",
            "transaction_token": transaction.token,
            "redirect_url": redirect_url
        })

    except TransbankError as e:
        return jsonify({"status": "Error en la transacción de pago", "error": str(e)})


@app.route("/api/v1/orders/commit", methods=["POST"])
def commit_order():
    transaction_token = request.json.get("transaction_token")

    # Obtener el pedido desde la base de datos
    order = order_collection.find_one({'transaction_token': transaction_token})
    if not order:
        return jsonify({"status": "Pedido no encontrado"}), 404

    try:
        # Confirmar la transacción en Webpay Plus
        transaction = Transaction.commit(
            token=transaction_token,
            commerce_code=commerce_code,
            api_key=api_key,
            integration_type=integration_type
        )

        if isinstance(transaction, dict) and transaction.get('vci') == 'TSY':
            # Actualizar el estado del pedido en la base de datos
            order_collection.update_one(
                {'transaction_token': transaction_token},
                {'$set': {'status': 'COMMITED'}}
            )
            return jsonify({"status": "Transacción confirmada con éxito"})
        else:
            return jsonify({"status": "Error en la confirmación de la transacción"})

    except TransbankError as e:
        return jsonify({"status": "Error en la transacción de pago", "error": str(e)})


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
