from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://isbravo:<password>@cluster1.kabn980.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


app = Flask(__name__)
api = Api(app)

clientes = [
    {
        'id': 1,
        'nombre': 'Juan',
        'apellido1': 'andes',
        'apellido2': 'feranades',
        'DNI': '12345678A'
    },
    {
        'id': 2,
        'nombre': 'isaac',
        'apellido1': 'peres',
        'apellido2': 'bravo',
        'DNI': '87654321B'
    },

]

cliente_parser = reqparse.RequestParser()

cliente_parser.add_argument('nombre', type=str, required=True, help='El campo nombre es obligatorio')
cliente_parser.add_argument('apellido1', type=str, required=True, help='El campo apellido1 es obligatorio')
cliente_parser.add_argument('apellido2', type=str, required=True, help='El campo apellido2 es obligatorio')
cliente_parser.add_argument('DNI', type=str, required=True, help='El campo DNI es obligatorio')

def buscar_cliente_por_id(id):

    for cliente in clientes:
        if cliente['id'] == id:
            return cliente
    return None


class Clientes(Resource):

    def get(self):

        return jsonify(clientes)
    
    def post(self):
        global clientes
        nuevo_cliente = {
            'id': clientes[-1]['id'] + 1,
            'nombre': request.json['nombre'],
            'apellido1': request.json['apellido1'],
            'apellido2': request.json['apellido2'],
            'DNI': request.json['DNI']
        }
        clientes.append(nuevo_cliente)
        return jsonify(nuevo_cliente)

class Cliente(Resource):

    def get(self, id):

        cliente = buscar_cliente_por_id(id)
        if cliente:
            return jsonify(cliente)
        else:
            abort(404, message=f'Cliente con ID {id} no encontrado')
    
    def put(self, id):

        cliente = buscar_cliente_por_id(id)
        if cliente:
            args = cliente_parser.parse_args()

            cliente['nombre'] = args['nombre']
            cliente['apellido1'] = args['apellido1']
            cliente['apellido2'] = args['apellido2']
            cliente['DNI'] = args['DNI']
            
            return jsonify(cliente)
        
        else:
            abort(404, message=f'Cliente con ID {id} no encontrado')
    
    def delete(self, id):
        global clientes
        cliente = buscar_cliente_por_id(id)
        if cliente:
            clientes = [c for c in clientes if c['id'] != id]
            return {'message': f'Cliente con ID {id} eliminado correctamente'}
        else:
            abort(404, message=f'Cliente con ID {id} no encontrado')


api.add_resource(Clientes, '/clientes')

api.add_resource(Cliente, '/clientes/<int:id>')


if __name__ == '__main__':

    app.run(debug=True)
