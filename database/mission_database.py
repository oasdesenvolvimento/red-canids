import json
import datetime
import core.model as model


def add_mission(value):
    response = model.mission_model.Mission(
        name_mission=value.name_mission,
        description_mission=value.description_mission,
        image_mission=value.image_mission,
        expiration_date=value.expiration_date,
        classification=value.classification,
        points=value.points,
        type_points=value.type_points,
        type_mission=value.type_mission,
        time_mission=value.time_mission,
        url_mission=value.url_mission,
        videos_mission=value.videos_mission,
        video_source=value.video_source,
        code_mission=value.code_mission,
        created_at=str(datetime.datetime.now()),
        updated_at=str(datetime.datetime.now())
    ).save()
    return str(response.auto_id_0)


def return_all_mission():
    response_database = model.mission_model.Mission.objects().to_json()
    response_database = json.loads(response_database)
    return response_database


def return_mission_by_id(id_mission):
    response_database = model.mission_model.Mission.objects(_id=id_mission).first().to_json()
    response_database = json.loads(response_database)
    return response_database


def validate_mission_finder(id_mission, code):
    response_database = model.mission_model.Mission.objects(_id=id_mission).first()
    if response_database is None:
        return None
    if response_database.code_mission == code:
        return True
    return False


def update_mission_by_id(id_mission, value):
    response_database = model.mission_model.Mission.objects(_id=id_mission).update_one(
        name_mission=value.name_mission,
        description_mission=value.description_mission,
        image_mission=value.image_mission,
        expiration_date=value.expiration_date,
        classification=value.classification,
        points=value.points,
        type_points=value.type_points,
        type_mission=value.type_mission,
        time_mission=value.time_mission,
        url_mission=value.url_mission,
        videos_mission=value.videos_mission,
        video_source=value.video_source,
        code_mission=value.code_mission,
        updated_at=str(datetime.datetime.now())
    )
    return response_database


def delete_mission_by_id(id_mission):
    response_database = model.mission_model.Mission.objects(_id=id_mission)
    response = response_database.delete()
    return response