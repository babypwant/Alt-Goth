from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os

api_url = os.getenv('REACT_APP_API_URL')


if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__, static_folder='../frontend/build')
CORS(app)

@app.route('/')
def index():
    return f'The API URL is: {api_url}'

@app.route('/static/js/<path:path>')
def serve_js(path):
    return send_from_directory(app.static_folder + '/static/js', path)

@app.route('/static/css/<path:path>')
def serve_css(path):
    return send_from_directory(app.static_folder + '/static/css', path)

# serve product data as JSON
@app.route('/api/products')
def products():
    # TODO: Replace with actual product data
    products = [
        {'id': 1, 'name': 'T-Shirt', 'price': 19.99},
        {'id': 2, 'name': 'Jeans', 'price': 49.99},
        {'id': 3, 'name': 'Jacket', 'price': 99.99},
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
