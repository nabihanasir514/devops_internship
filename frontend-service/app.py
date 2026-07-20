from flask import Flask, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

@app.route("/info")
def info():
    return jsonify({
        "service": "frontend-service",
        "version": "1.0.0",
        "description": "Frontend microservice"
    })

@app.route("/backend-info")
def backend_info():
    response = requests.get("http://localhost:5002/info")
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
