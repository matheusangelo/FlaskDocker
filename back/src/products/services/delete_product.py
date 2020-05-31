from products.commands import Product
from bson.objectid import ObjectId
from products.config import products_collection


def delete_product_request(id):
    try:
        products_collection.delete_one({"_id": ObjectId(id)})
        return "Deleted"

    except:
        return "Error"
