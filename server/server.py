# server/server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {"ShadowUnleashedGaming": "123456789"}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if users.get(username) == password:
        return jsonify({"success": True, "token": "admin-token"})
    return jsonify({"success": False, "message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
