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
