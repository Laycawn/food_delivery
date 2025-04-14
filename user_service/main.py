from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy database
users = []

# Endpoint: Register User
@app.route("/register", methods=["POST"])
def register_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username and password:
        # Check if username already exists
        for user in users:
            if user["username"] == username:
                return jsonify({"error": "Username already exists"}), 409  # Conflict
        # Add user to the database
        users.append({"username": username, "password": password})
        return jsonify({"message": f"User {username} registered successfully!"}), 201  # Created
    else:
        return jsonify({"error": "Invalid input"}), 400  # Bad Request

# Endpoint: Login User
@app.route("/login", methods=["POST"])
def login_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username and password:
        # Check credentials
        for user in users:
            if user["username"] == username and user["password"] == password:
                return jsonify({"message": f"Welcome, {username}!"}), 200  # OK
        return jsonify({"error": "Invalid credentials"}), 401  # Unauthorized
    else:
        return jsonify({"error": "Invalid input"}), 400  # Bad Request

# Health Check Endpoint (Optional but useful)
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "User service is up and running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

