# app.py
from flask import Flask, request, jsonify
import json
from bson import json_util
import os
import time
import redis
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the Flask
app = Flask(__name__)

# Load the Redis configuration
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = os.getenv("REDIS_PORT", 6379)

# Retry logic to wait for Redis to be ready
def get_redis_client():
    client = redis.Redis(host=redis_host, port=redis_port)
    for _ in range(5):
        try:
            client.ping()
            return client
        except redis.exceptions.ConnectionError:
            time.sleep(1)
    raise Exception("Could not connect to Redis")

redis_client = get_redis_client()

# Home Page
@app.route("/")
def index():
    count = redis_client.incr('counter')
    return f'Flask Application home Page visited {count} times.'

# # Register the product blueprint
# app.register_blueprint(product_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


