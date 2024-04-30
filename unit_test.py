import unittest
from app import add_product_to_database, calculate_cart_total

class TestBackendFunctions(unittest.TestCase):
    def test_add_product_to_database(self):
        # Test adding a product to the database
        product_id = add_product_to_database("Test Product", 9.99)
        self.assertIsInstance(product_id, int)  # Check if product_id is an integer

        # Test adding another product with the same name and price
        product_id_duplicate = add_product_to_database("Test Product", 9.99)
        self.assertNotEqual(product_id_duplicate, product_id)  # Check if product_id is unique

    def test_calculate_cart_total(self):
        # Test calculating total price of items in an empty cart
        cart_empty = []
        total_empty = calculate_cart_total(cart_empty)
        self.assertEqual(total_empty, 0)  # Total should be 0 for an empty cart

        # Test calculating total price of items in a non-empty cart
        cart = [{"price": 10.99, "quantity": 2}, {"price": 20.99, "quantity": 1}]
        total = calculate_cart_total(cart)
        expected_total = 10.99 * 2 + 20.99 * 1
        self.assertEqual(total, expected_total)  # Total should match the expected total

if __name__ == '__main__':
    unittest.main()
