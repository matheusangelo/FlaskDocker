import products.services as service

from flask import Blueprint, request
from .config import mongo
from .commands import Product

products_v1 = Blueprint('products_v1', __name__, url_prefix='/v1/products')


@products_v1.route('/create', methods=['POST'])
def create():
    return service.create_product_request(schema=Product, data=request.get_json())


@products_v1.route('/<id>', methods=['DELETE'])
def update(id):
    return service.delete_product_request(id)


@products_v1.route('/<id>', methods=['PUT'])
def delete(id):
    return service.update_product_request(schema=Product, data=request.get_json(), id=id)


@products_v1.route('/', methods=['GET'])
def get_all():
    return service.get_all_product_request()


@products_v1.route('/<id>', methods=['GET'])
def get_by_id(id):
    return service.get_product_by_id_request(id)
