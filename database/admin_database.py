import json
import random
import datetime
import internal
import core.model as model
import core.schema.admin_account as admin_schema


def add_new_admin(value: admin_schema.admin_account_post_schema):
    """
    Add new admin in database
    :param value:
    :return:
    """
    check_email = model.admin_account_model.Admin.objects(email=value.email).first()
    if check_email is not None:
        return 401
    response = model.admin_account_model.Admin(
        name=value.name,
        email=value.email,
        password=internal.crypt.encrypt(value.password) if len(value.password) > 0 else "",
        level_access=value.level_access
    ).save()
    return response.auto_id_0


def return_admin_by_email(email):
    """
    Return user in database by email
    :return: json
    """
    response_database = model.admin_account_model.Admin.objects(email=email).first()
    response_database = json.loads(response_database.to_json()) if response_database is not None else None
    return response_database


def return_admin_by_login(email: str, password: str):
    """
    Return admin by email and password
    :param email:
    :param password:
    :return:
    """
    get_admin_by_email = return_admin_by_email(email)
    if get_admin_by_email is not None:
        get_password_encrypted = internal.crypt.dcrypt(get_admin_by_email["password"].encode("utf-8"))
        response_database = model.admin_account_model.Admin.objects(email=email).first()
        response_database = json.loads(response_database.to_json()) if response_database is not None else None
        if response_database["email"] == email and get_password_encrypted == password:
            return response_database