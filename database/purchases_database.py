import json
import datetime
import core.model as model


def add_purchases(value):
    """
    add new purchases
    :param value:
    :return:
    """
    response = model.purchases_model.Purchases(
        name=value.name,
        description=value.description,
        id_product=value.id_product,
        id_account=value.id_account,
        last_account_red_coins=value.last_account_red_coins,
        current_account_red_coins=value.current_account_red_coins,
        total_price=value.total_price,
        is_visible=True,
        is_done=False,
        created_at=str(datetime.datetime.now()),
        updated_at=str(datetime.datetime.now())
    ).save()
    return str(response.auto_id_0)


def return_all_purchases():
    response_database = model.purchases_model.Purchases.objects().to_json()
    response_database = json.loads(response_database)
    return response_database


def return_purchase_by_id(id_purchase):
    response_database = model.purchases_model.Purchases.objects(_id=id_purchase).first().to_json()
    response_database = json.loads(response_database)
    return response_database


def update_purchase_by_id(id_purchase, value):
    response_database = model.purchases_model.Purchases.objects(_id=id_purchase).update_one(
        name=value.name,
        description=value.description,
        id_product=value.id_product,
        id_account=value.id_account,
        last_account_red_coins=value.last_account_red_coins,
        current_account_red_coins=value.current_account_red_coins,
        total_price=value.total_price,
        updated_at=str(datetime.datetime.now())
    )
    return response_database


def update_purchase_done_visible(id_purchase):
    response_database = model.purchases_model.Purchases.objects(_id=id_purchase).update_one(
        is_visible=False,
        is_done=True,
    )
    return response_database


def delete_purchase_by_id(id_purchase):
    response_database = model.purchases_model.Purchases.objects(_id=id_purchase)
    response = response_database.delete()
    return response