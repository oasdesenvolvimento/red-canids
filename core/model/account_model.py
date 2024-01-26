from mongoengine import (Document, ObjectIdField, StringField, IntField, ListField,
                         EmbeddedDocument, EmbeddedDocumentField)


class MissionsCompleted(EmbeddedDocument):
    id_mission = StringField()
    date_completed = StringField()
    points = IntField()
    type_points = StringField()


class Account(Document):
    _id = ObjectIdField()
    name = StringField()
    email = StringField()
    password = StringField()
    red_coins = IntField()
    red_xp = IntField()
    background_photo = StringField()
    friends = ListField()
    genre = StringField()
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
    missions_completed = ListField(EmbeddedDocumentField(MissionsCompleted))
