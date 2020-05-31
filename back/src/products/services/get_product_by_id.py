from products.config import products_collection
from bson.objectid import ObjectId
from products.commands import Product


def get_product_by_id_request(id):
    retorno = []

    for produto in products_collection.find({"_id": ObjectId(id)}):
        retorno.append(produto)

    return Product().dump(retorno[0])
