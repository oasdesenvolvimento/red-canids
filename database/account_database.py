import json
import random
import datetime
import core.model as model
import core.schema.account as account_schema


def add_new_account(value: account_schema.account_post_schema):
    """
    Add new account in database
    :return:
    """
    check_email = model.account_model.Account.objects(email=value.email).first()
    if check_email is not None:
        return 401
    response = model.account_model.Account(
        name=value.name,
        email=value.email,
        password=value.password,
        red_coins=value.red_coins,
        red_xp=value.red_xp,
        gmail_access_token=value.gmail_access_token,
        apple_access_token=value.apple_access_token,
        facebook_access_token=value.facebook_access_token,
        discord_access_token=value.discord_access_token,
        twitter_access_token=value.twitter_access_token,
        photo_profile=value.photo_profile,
        birthday=value.birthday,
        bio=value.bio,
        code_access=str(random.randint(100000, 999999)),
        created_at=str(datetime.datetime.now()),
        updated_at=str(datetime.datetime.now())
    ).save()
    print(response.auto_id_0)
    return {
        "_id": str(response.auto_id_0),
        "code_access": str(response.code_access),
    }


def return_all_account():
    """
    Return all accounts in database
    :return:
    """
    response_database = model.account_model.Account.objects().to_json()
    response_database = json.loads(response_database)
    return response_database


def return_account_by_email_and_code_access(email: str, code_access: str):
    """
    Return account by email and code access
    :param email:
    :param code_access:
    :return:
    """
    response_database = model.account_model.Account.objects(email=email, code_access=code_access).first()
    if response_database is None:
        return None
    response_database = response_database.to_json()
    response_database = json.loads(response_database)
    return response_database


def update_mission_completed(value):
    """
    Update mission completed, the value will be updated the list of missions completed
    :param value:
    :return:
    """
    response_database = model.account_model.Account.objects(_id=value.id_account).first()
    if response_database is None:
        return None
    # Check if mission already completed
    for mission in response_database.missions_completed:
        if mission.id_mission == value.id_mission:
            return None
    # Check if mission is valid
    check_mission = model.mission_model.Mission.objects(_id=value.id_mission).first()
    if check_mission is None:
        return None
    response_database.missions_completed.append(
        model.account_model.MissionsCompleted(
            id_mission=value.id_mission,
            date_completed=str(datetime.datetime.now()),
            points=value.points,
            type_points=value.type_points
        )
    )
    response_database.save()
    response_database = response_database.to_json()
    response_database = json.loads(response_database)

    # Get the type_point of check_mission and update the red_coins or red_xp
    if check_mission["type_points"] == "red_coins":
        response_database["red_coins"] = response_database["red_coins"] + check_mission["points"]
    elif check_mission["type_points"] == "red_xp":
        response_database["red_xp"] = response_database["red_xp"] + check_mission["points"]
    else:
        return None
    model.account_model.Account.objects(_id=value.id_account).update_one(
        red_coins=response_database["red_coins"],
        red_xp=response_database["red_xp"]
    )
    return response_database


def check_if_mission_already_completed(id_account: str, id_mission: str):
    """
    Check if mission already completed
    :param id_account:
    :param id_mission:
    :return:
    """
    response_database = model.account_model.Account.objects(_id=id_account).first()
    if response_database is None:
        return None
    for mission in response_database.missions_completed:
        if mission.id_mission == id_mission:
            return True
    return False
