from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

mongo_url = os.getenv("MONGO_URL")
client = MongoClient(mongo_url)

db = client["todo_db"]
collection = db["todo_items"]


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.json

    item = {
        "item_name": data.get("item_name"),
        "description": data.get("description")
    }

    collection.insert_one(item)

    return jsonify({
        "message": "Todo item submitted successfully"
    }), 201


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8002)
