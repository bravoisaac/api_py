import unittest
from flask import Flask
from flask_jwt_extended import JWTManager
from app import app

class ClientAPITestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['JWT_SECRET_KEY'] = 'test-secret-key'
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_create_existing_user(self):
        response = self.app.post('/api/v1/users', json={
            "username": "testuser",
            "password": "testpassword"
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["status"], "Usuario ya existe")

    def test_login(self):
        response = self.app.post('/api/v1/login', json={
            "username": "testuser",
            "password": "testpassword"
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", data)

    def test_invalid_credentials(self):
        response = self.app.post('/api/v1/login', json={
            "username": "testuser",
            "password": "wrongpassword"
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data["msg"], "Credenciales incorrectas")

    def test_get_all_users(self):
        response = self.app.get('/api/v1/usersAll')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)



if __name__ == '__main__':
    unittest.main()
