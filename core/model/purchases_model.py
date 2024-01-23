from mongoengine import Document, ObjectIdField, StringField, IntField, ListField, BooleanField


class Purchases(Document):
    _id = ObjectIdField()
    name = StringField()
    description = StringField()
    id_product = StringField()
    id_account = StringField()
    last_account_red_coins = IntField()
    current_account_red_coins = IntField()
    total_price = IntField()
    is_visible = BooleanField()
    is_done = BooleanField()
    created_at = StringField()
    updated_at = StringField()