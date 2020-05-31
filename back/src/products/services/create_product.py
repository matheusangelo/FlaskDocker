from products.commands import Product
from products.config import products_collection


def create_product_request(schema, data):
    try:
        products_collection.insert_one(Product().load(data))
        return "Created"

    except:
        return "Error"
