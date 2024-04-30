import unittest
import json
from app import app

class TestAPIFunctions(unittest.TestCase):
    def setUp(self):
        # Set up test client
        self.client = app.test_client()

    def test_add_product(self):
        # Simulate adding a product using the test client
        data = {'name': 'New Product', 'price': 9.99}
        response = self.client.post('/products', json=data)

        # Verify the response status code
        self.assertEqual(response.status_code, 201)  # Check if product is added successfully

        # Verify the response message
        data = response.json
        self.assertIn('message', data)  # Check if response contains a 'message' key
        self.assertEqual(data['message'], 'Product added successfully')  # Check if message is as expected

    # Add more API function test cases as needed

if __name__ == '__main__':
    unittest.main()
