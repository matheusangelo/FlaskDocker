from marshmallow import fields, Schema


class Product(Schema):
    _id = fields.Str()
    name = fields.Str()
    description = fields.Str()
    rate = fields.Number()
