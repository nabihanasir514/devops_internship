from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "service": "backend-service",
        "status": "UP",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }), 200


@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "service": "backend-service",
        "version": "1.0.0",
        "description": "Backend microservice",
        "language": "Python",
        "framework": "Flask"
    }), 200


# Example API that the frontend can call
@app.route("/message", methods=["GET"])
def message():
    return jsonify({
        "message": "Hello from the Backend Service!",
        "service": "backend-service"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
