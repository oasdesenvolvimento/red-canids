from mongoengine import Document, ObjectIdField, StringField, IntField, ListField, BooleanField


class Product(Document):
    _id = ObjectIdField()
    name_product = StringField()
    description_product = StringField()
    price = IntField()
    image_product = StringField()
    date_expiration = StringField()
    is_enabled = BooleanField()
    stock = IntField()
    classification = StringField()
    type_product = StringField()
    code_product = StringField()
    created_at = StringField()
    updated_at = StringField()
