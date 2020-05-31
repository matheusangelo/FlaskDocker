from flask import jsonify
from products.commands import Product
from products.config import products_collection
from bson.objectid import ObjectId
from products.commands import Product


def update_product_request(schema, data, id):
    dados = Product().load(data)

    filtro = {"_id": ObjectId(id)}

    novos_valores = {"$set": dados}

    products_collection.update_one(filtro, novos_valores)

    return "updated"
