# geocaching_app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample geocache data (Replace with a database in a real application)
geocaches = [
    {"id": 1, "name": "Cache 1", "latitude": 37.7749, "longitude": -122.4194},
    {"id": 2, "name": "Cache 2", "latitude": 37.7749, "longitude": -122.4094},
    {"id": 3, "name": "Cache 3", "latitude": 37.7849, "longitude": -122.4094},
]

@app.route("/")
def index():
    return render_template("index.html", geocaches=geocaches)

@app.route("/add_geocache", methods=["POST"])
def add_geocache():
    data = request.get_json()
    new_geocache = {
        "id": len(geocaches) + 1,
        "name": data["name"],
        "latitude": data["latitude"],
        "longitude": data["longitude"],
    }
    geocaches.append(new_geocache)
    return jsonify({"message": "Geocache added successfully"})

if __name__ == "__main__":
    app.run(debug=True)
