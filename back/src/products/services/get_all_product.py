from flask import jsonify
from products.commands import Product
from products.config import products_collection


def get_all_product_request():
    retorno = []

    for product in products_collection.find():
        retorno.append(product)

    lista = Product().dump(retorno, many=True)

    return jsonify(lista)
