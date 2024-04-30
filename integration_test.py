import unittest
from app import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        # Set up test client
        self.client = app.test_client()

    def test_add_product_to_database_and_get_all_products(self):
        # Add a product to the database
        response = self.client.post('/products', json={"name": "New Product", "price": 9.99})
        self.assertEqual(response.status_code, 201)  # Check if product is added successfully

        # Retrieve all products
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)  # Check if request is successful

        # Check if the newly added product is in the list of products
        data = response.json
        self.assertIn("New Product", [product["name"] for product in data])  # Check if product name is in response

if __name__ == '__main__':
    unittest.main()
