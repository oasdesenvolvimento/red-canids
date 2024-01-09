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
