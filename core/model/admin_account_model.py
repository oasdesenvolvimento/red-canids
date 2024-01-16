from mongoengine import Document, ObjectIdField, StringField, IntField


class Admin(Document):
    _id = ObjectIdField()
    name = StringField()
    email = StringField()
    password = StringField()
    level_access = IntField()
