import unittest
import json
from app import app

class TestAPIValidation(unittest.TestCase):
    def setUp(self):
        # Set up test client
        self.client = app.test_client()

    def test_get_all_products_response(self):
        response = self.client.get('/products')
        data = json.loads(response.data)

        # Validate response schema
        self.assertIsInstance(data, list)  # Check if response is a list
        for product in data:
            self.assertIsInstance(product, dict)  # Check if each product is a dictionary
            self.assertIn('id', product)  # Check if each product has an 'id' key
            self.assertIsInstance(product['id'], int)  # Check if 'id' is an integer
            self.assertIn('name', product)  # Check if each product has a 'name' key
            self.assertIsInstance(product['name'], str)  # Check if 'name' is a string
            self.assertIn('price', product)  # Check if each product has a 'price' key
            self.assertIsInstance(product['price'], (float, int))  # Check if 'price' is a float or an integer

    # Add more API validation test cases as needed

if __name__ == '__main__':
    unittest.main()
