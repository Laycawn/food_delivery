from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# In-memory database for orders
orders = []

# Endpoint: Create a new order
@app.route("/createOrder", methods=["POST"])
def create_order():
    data = request.json
    order_id = data.get("order_id")
    item = data.get("item")
    quantity = data.get("quantity")

    if order_id and item and quantity:
        orders.append({"order_id": order_id, "item": item, "quantity": quantity})
        return jsonify({"message": f"Order {order_id} created successfully!"}), 201
    else:
        return jsonify({"error": "Invalid input"}), 400

# Endpoint: Get all orders
@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify({"orders": orders}), 200

# Endpoint: Test communication with user-service
@app.route("/testUserService", methods=["GET"])
def test_user_service():
    try:
        # Querying the /health endpoint of user-service
        response = requests.get("http://user-service:8000/health")
        if response.status_code == 200:
            return jsonify({
                "message": "User Service is reachable!",
                "data": response.json()
            }), 200
        else:
            return jsonify({
                "error": "Failed to reach User Service",
                "status_code": response.status_code
            }), 500
    except Exception as e:
        return jsonify({"error": f"Exception: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)

