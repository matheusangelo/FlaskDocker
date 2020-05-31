import os

from products import products_v1
from flask import Flask, Blueprint
from pymongo import MongoClient

app = Flask(__name__)
app.register_blueprint(products_v1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True)
