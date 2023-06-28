"""import unittest
from flask import Flask
from flask_jwt_extended import JWTManager
from appCompra import app

class PurchaseAPITestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['JWT_SECRET_KEY'] = 'test-secret-key'
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_create_order(self):
        response = self.app.post('/api/v1/orders', json={
            "users_id": "user_id",
            "produc_id": "product_id",
            "quantity": 1
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "Pedido creado con éxito")

    def test_create_order_invalid_client(self):
        response = self.app.post('/api/v1/orders', json={
            "users_id": "invalid_user_id",
            "produc_id": "product_id",
            "quantity": 1
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["status"], "Cliente no encontrado")

    def test_create_order_invalid_product(self):
        response = self.app.post('/api/v1/orders', json={
            "users_id": "user_id",
            "produc_id": "invalid_product_id",
            "quantity": 1
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["status"], "Producto no encontrado")

    def test_create_order_insufficient_stock(self):
        response = self.app.post('/api/v1/orders', json={
            "users_id": "user_id",
            "produc_id": "product_id",
            "quantity": 10
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["status"], "Stock insuficiente")

    def test_update_order(self):
        response = self.app.put('/api/v1/order/<order_id>', json={
            "cliente_id": "new_user_id",
            "product_id": "new_product_id",
            "quantity": 2
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "Pedido actualizado con éxito")

    def test_update_order_invalid_client(self):
        response = self.app.put('/api/v1/order/<order_id>', json={
            "cliente_id": "invalid_user_id",
            "product_id": "new_product_id",
            "quantity": 2
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["status"], "Cliente no encontrado")

    def test_update_order_invalid_product(self):
        response = self.app.put('/api/v1/order/<order_id>', json={
            "cliente_id": "new_user_id",
            "product_id": "invalid_product_id",
            "quantity": 2
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data["status"], "Producto no encontrado")

    def test_update_order_insufficient_stock(self):
        response = self.app.put('/api/v1/order/<order_id>', json={
            "cliente_id": "new_user_id",
            "product_id": "new_product_id",
            "quantity": 10
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data["status"], "Stock insuficiente")

    def test_delete_order(self):
        response = self.app.delete('/api/v1/order/<order_id>')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
"""