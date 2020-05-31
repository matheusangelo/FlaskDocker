import os
from pymongo import MongoClient


# connection
mongo = MongoClient('mongodb://db')


# databases
db = mongo['Sample']


# collections

products_collection = db['products']
