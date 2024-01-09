import random
import datetime
import core.model as model
import core.schema.account as account_schema


def add_new_account(value: account_schema.account_post_schema):
    """
    Add new account in database
    :return:
    """
    response = model.account_model.Account(
        name=value.name,
        email=value.email,
        password=value.password,
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
