from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

productos = [
    {
        'id': 1,
        'marca': 'lenovo',
        'nombre': 'note',
        'precio': 150000,
        'descripcion': 'pc note'
    },
    {
        'id': 2,
        'marca': 'lenovo',
        'nombre': 'mause',
        'precio': 13000,
        'descripcion': 'mause de pc'
    }
]

producto_parser = reqparse.RequestParser()

producto_parser.add_argument('nombre', type=str, required=True, help='El campo nombre es obligatorio')
producto_parser.add_argument('marca', type=str, required=True, help='El campo marca es obligatorio')
producto_parser.add_argument('precio', type=float, required=True, help='El campo precio es obligatorio')
producto_parser.add_argument('descripcion', type=str, required=True, help='El campo descripcion es obligatorio')

def buscar_producto_por_id(id):
    for producto in productos:
        if producto['id'] == id:
            return producto
    return None


class Productos(Resource):

    def get(self):
        return jsonify(productos)
    
    def post(self):
        global productos
        nuevo_producto = {
            'id': productos[-1]['id'] + 1,
            'nombre': request.json['nombre'],
            'marca': request.json['marca'],
            'precio': request.json['precio'],
            'descripcion': request.json['descripcion']
        }
        productos.append(nuevo_producto)
        return jsonify(nuevo_producto)

class Producto(Resource):

    def get(self, id):
        producto = buscar_producto_por_id(id)
        if producto:
            return jsonify(producto)
        else:
            abort(404, message=f'Producto con ID {id} no encontrado')
    
    def put(self, id):
        producto = buscar_producto_por_id(id)
        if producto:
            args = producto_parser.parse_args()
            producto['nombre'] = args['nombre']
            producto['marca'] = args['marca']
            producto['precio'] = args['precio']
            producto['descripcion'] = args['descripcion']
            return jsonify(producto)
        else:
            abort(404, message=f'Producto con ID {id} no encontrado')
    
    def delete(self, id):
        global productos
        producto = buscar_producto_por_id(id)
        if producto:
            productos = [p for p in productos if p['id'] != id]
            return {'message': f'Producto con ID {id} eliminado correctamente'}
        else:
            abort(404, message=f'Producto con ID {id} no encontrado')


api.add_resource(Productos, '/productos')
api.add_resource(Producto, '/productos/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)
