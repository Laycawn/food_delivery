from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy restaurant database
restaurants = [
    {"id": 1, "name": "Pasta Palace", "menu": {"Spaghetti": 12, "Ravioli": 15}},
    {"id": 2, "name": "Burger Haven", "menu": {"Cheeseburger": 10, "Fries": 5}},
]

# Endpoint: List all restaurants
@app.route("/listRestaurants", methods=["GET"])
def list_restaurants():
    return jsonify({"restaurants": restaurants}), 200

# Endpoint: Get menu of a specific restaurant
@app.route("/getMenu", methods=["GET"])
def get_menu():
    restaurant_id = request.args.get("restaurant_id")
    if restaurant_id:
        for restaurant in restaurants:
            if str(restaurant["id"]) == restaurant_id:
                return jsonify({"menu": restaurant["menu"]}), 200
        return jsonify({"error": "Restaurant not found"}), 404
    else:
        return jsonify({"error": "Missing restaurant_id parameter"}), 400

# Endpoint: Update menu (Admin functionality)
@app.route("/updateMenu", methods=["POST"])
def update_menu():
    data = request.json
    restaurant_id = data.get("restaurant_id")
    new_menu = data.get("menu")
    if restaurant_id and new_menu:
        for restaurant in restaurants:
            if restaurant["id"] == restaurant_id:
                restaurant["menu"] = new_menu
                return jsonify({"message": f"Menu updated for restaurant {restaurant_id}"}), 200
        return jsonify({"error": "Restaurant not found"}), 404
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
