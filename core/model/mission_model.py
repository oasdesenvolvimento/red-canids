from mongoengine import Document, ObjectIdField, StringField, IntField, ListField


class Mission(Document):
    _id = ObjectIdField()
    name_mission = StringField()
    description_mission = StringField()
    image_mission = StringField()
    expiration_date = StringField()
    classification = StringField()
    points = IntField()
    type_points = StringField()
    type_mission = StringField()
    time_mission = StringField()
    url_mission = StringField()
    videos_mission = ListField()
    video_source = StringField()
    code_mission = StringField()
    created_at = StringField()
    updated_at = StringField()
