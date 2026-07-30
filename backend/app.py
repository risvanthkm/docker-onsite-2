from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)

log_file = "users.log"

@app.route("/")
def home():
    container_name = os.getenv("CONTAINER_NAME", "unknown-container")
    user_id = request.headers.get("X-User-ID", "Anonymous")

    with open(log_file, 'a') as f:
        now = datetime.now()
        f.write(f'[{now}] | USER_ID:{user_id} | Server:{container_name}\n')

    return f"Hello, User: {user_id}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9090, debug=True)