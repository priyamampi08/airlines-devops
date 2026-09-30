from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "Airline Booking API",
        "message": "Airline DevOps project is running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/flights")
def flights():
    return jsonify([
        {
            "flight": "AI101",
            "from": "DEL",
            "to": "BOM",
            "status": "ON_TIME"
        },
        {
            "flight": "AI202",
            "from": "BOM",
            "to": "BLR",
            "status": "ON_TIME"
        },
        {
            "flight": "AI303",
            "from": "CCU",
            "to": "DEL",
            "status": "DELAYED"
        }
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)