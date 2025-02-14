from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_news

app = Flask(__name__)
CORS(app)  # Allow frontend requests

@app.route("/get_news", methods=["GET"])
def get_news():
    state = request.args.get("state", "").lower()
    news = scrape_news(state)
    return jsonify(news)

if __name__ == "__main__":
    app.run(debug=True)
