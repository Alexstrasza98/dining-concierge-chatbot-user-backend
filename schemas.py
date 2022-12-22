from marshmallow import Schema, fields


# Plain schema has no relationship between schemas
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class UserRegisterSchema(UserSchema):
    email = fields.Str(required=True)


class SavedRestaurantSchema(Schema):
    id = fields.Integer(dump_only=True)
    businessId = fields.Str(required=True)
    name = fields.Str(required=True)
    rate = fields.Float(required=True)
    location = fields.Str(required=True)
    price = fields.Str()
    image_url = fields.Str(required=True)
    yelp_url = fields.Str(required=True)