from flask import Flask, jsonify

app = Flask(__name__)

# Root endpoint
@app.route('/')
def home():
    return "Welcome to the User Service!", 200

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "User service is up and running"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

