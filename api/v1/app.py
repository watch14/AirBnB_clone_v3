#!/usr/bin/python3
""" app """

from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown():
    """ Tear It Down To The Ground """
    storage.close()


if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST")
    port = os.getenv("HBNB_API_PORT")

    if not host:
        host = 0.0.0.0
    if not port:
        port = 5000

    app.run(host=host, port=port, threaded=True)
