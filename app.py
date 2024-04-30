from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for products and cart (to be replaced with database operations)
products = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 20.99},
    # Add more products as needed
]

cart = []

def add_product_to_database(name, price):
    # Placeholder function to add a product to the database
    # This function will be implemented later
    # For now, it returns True to indicate success
    product_id = len(products) + 1
    product = {"id": product_id, "name": name, "price": price}
    products.append(product)
    return product_id

# Function to calculate the total price of items in the cart
def calculate_cart_total(cart):
    # Placeholder function to calculate the total price of items in the cart
    # This function will be implemented later
    # For now, it returns 0 as the total
    total = sum(item['price'] * item['quantity'] for item in cart)
    return total

# Endpoints for managing products
@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    product_id = add_product_to_database(data.get('name'), data.get('price'))
    return jsonify({"message": "Product added successfully", "product_id": product_id}), 201


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p['id'] != product_id]
    return jsonify({"message": "Product deleted successfully"})

# Endpoints for managing the cart
@app.route('/cart', methods=['GET'])
def get_cart():
    return jsonify(cart)

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.json
    cart.append(data)
    return jsonify({"message": "Product added to cart successfully"}), 201

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.json
    global cart
    cart = [item for item in cart if item['id'] != data['id']]
    return jsonify({"message": "Product removed from cart successfully"})


if __name__ == '__main__':
    app.run(debug=True)
