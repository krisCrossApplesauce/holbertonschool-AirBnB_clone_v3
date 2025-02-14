#!/usr/bin/python3
""" 4. Status of your API """
from flask import Flask, jsonify, make_response
from flask_cors import CORS
import os
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_it_down(stuff):
    """ clost storage """
    storage.close()


@app.errorhandler(404)
def handle_404(error):
    """ displays 404 error """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
