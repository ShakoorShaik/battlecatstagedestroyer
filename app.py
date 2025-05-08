from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open("../data/raw_data.json") as f:
    cats = json.load(f)

@app.route("/api/cats", methods=["GET"])
def get_cats():
    return jsonify(cats)

@app.route("/api/strategy", methods=["POST"])
def get_strategy():
    stage = request.json.get("stage_traits")
    filtered = [cat for cat in cats if cat["trait"] in stage]
    return jsonify(filtered[:10])  # just return the first 10 matches for now

if __name__ == "__main__":
    app.run(debug=True)
