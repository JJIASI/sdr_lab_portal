from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


def authenticate(username):
    with open('/app/members.json') as f:
        data = json.load(f)
        if username in data:
            return True
    return False


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")

    if not username:
        return jsonify({"message": "Both username and password are required"}), 400

    if authenticate(username):
        with open('/app/token') as f:
            token = f.read()
        return jsonify({"message": "Login successful", "token": token}), 200
    else:
        return jsonify({"message": "Invalid username"}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
