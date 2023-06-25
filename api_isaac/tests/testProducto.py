import unittest
from flask import Flask
from flask_jwt_extended import JWTManager
from appProducto import app

class ProductAPITestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['JWT_SECRET_KEY'] = 'test-secret-key'
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_create_product(self):
        response = self.app.post('/api/v1/products', json={
            "name": "Test Product",
            "price": 10.99,
            "stock": 100
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "Producto creado con éxito")

    def test_get_all_products(self):
        response = self.app.get('/api/v1/productsAll')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_get_product(self):
        response = self.app.get('/api/v1/product/<product_id>')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    def test_get_nonexistent_product(self):
        response = self.app.get('/api/v1/product/nonexistent_product_id')
        self.assertEqual(response.status_code, 404)

    def test_update_product(self):
        response = self.app.put('/api/v1/product/<product_id>', json={
            "name": "Updated Product",
            "price": 15.99,
            "stock": 50
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "Producto actualizado con éxito")

    def test_update_nonexistent_product(self):
        response = self.app.put('/api/v1/product/nonexistent_product_id', json={
            "name": "Updated Product",
            "price": 15.99,
            "stock": 50
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_product(self):
        response = self.app.delete('/api/v1/product/<product_id>')
        self.assertEqual(response.status_code, 204)

    def test_delete_nonexistent_product(self):
        response = self.app.delete('/api/v1/product/nonexistent_product_id')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
