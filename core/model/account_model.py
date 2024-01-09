from mongoengine import Document, ObjectIdField, StringField, BooleanField, EmbeddedDocument, EmbeddedDocumentField


class Account(Document):
    _id = ObjectIdField()
    name = StringField()
    email = StringField()
    password = StringField()
    gmail_access_token = StringField()
    apple_access_token = StringField()
    facebook_access_token = StringField()
    discord_access_token = StringField()
    twitter_access_token = StringField()
    photo_profile = StringField()
    birthday = StringField()
    bio = StringField()
    code_access = StringField()
    created_at = StringField()
    updated_at = StringField()
