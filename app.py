import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Render!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Use Render's assigned port or 10000 for local testing
    app.run(host='0.0.0.0', port=port)
