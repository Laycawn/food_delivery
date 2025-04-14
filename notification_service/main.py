from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy notification log
notifications = []

# Endpoint: Send a notification
@app.route("/sendNotification", methods=["POST"])
def send_notification():
    data = request.json
    recipient = data.get("recipient")
    message = data.get("message")
    if recipient and message:
        notifications.append({"recipient": recipient, "message": message})
        return jsonify({"message": f"Notification sent to {recipient}"}), 200
    else:
        return jsonify({"error": "Invalid input"}), 400

# Endpoint: View all notifications
@app.route("/viewNotifications", methods=["GET"])
def view_notifications():
    return jsonify({"notifications": notifications}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)
