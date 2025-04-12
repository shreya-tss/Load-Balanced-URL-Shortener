
from flask import Flask, request, redirect, jsonify
import redis
import string
import random
import os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'redis')
r = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)

BASE_URL = "http://localhost:5000/"

def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the URL Shortener!",
        "usage": {
            "shorten_url": {
                "endpoint": "/shorten",
                "method": "POST",
                "body_format": {"url": "https://example.com"}
            },
            "redirect": {
                "endpoint": "/<short_id>",
                "method": "GET"
            }
        }
    }), 200

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    if not original_url:
        return jsonify({'error': "Missing URL"}), 400

    short_id = generate_short_id()
    while r.exists(short_id):
        short_id = generate_short_id()

    r.set(short_id, original_url)
    short_url = BASE_URL + short_id
    return jsonify({'short_url': short_url}), 200

@app.route('/<short_id>', methods=['GET'])
def redirect_url(short_id):
    original_url = r.get(short_id)
    if original_url:
        return redirect(original_url)
    else:
        return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

