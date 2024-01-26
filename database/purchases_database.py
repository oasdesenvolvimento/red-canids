import json
import datetime
import core.model as model


def add_purchases(value):
    """
    add new purchases
    :param value:
    :return:
    """
    model.account_model.Account.objects(_id=value.id_account).update_one(
        red_coins=value.current_account_red_coins
    )
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
    response_account = model.account_model.Account.objects().to_json()
    response_account = json.loads(response_account)
    response_product = model.products_model.Product.objects().to_json()
    response_product = json.loads(response_product)
    response_database_merged = []
    response_database = json.loads(response_database)
    for item in response_database:
        try:
            response_database_account = \
                [account for account in response_account if account["_id"]["$oid"] == item["id_account"]][0]
        except Exception as e:
            response_database_account = None
        try:
            response_database_product = \
                [product for product in response_product if product["_id"]["$oid"] == item["id_product"]][0]
        except Exception as e:
            response_database_product = None
        if response_database_account is None or response_database_product is None:
            continue
        response_database_merged.append(
            {
                "purchase": item,
                "account": response_database_account,
                "product": response_database_product
            }
        )
    return response_database_merged


def return_purchase_by_id(id_purchase):
    response_database = model.purchases_model.Purchases.objects(_id=id_purchase).first().to_json()
    response_account = model.account_model.Account.objects().to_json()
    response_account = json.loads(response_account)
    response_product = model.products_model.Product.objects().to_json()
    response_product = json.loads(response_product)
    response_database = json.loads(response_database)
    response_database_merged = {
        "purchase": response_database,
        "account":
            [account for account in response_account if account["_id"]["$oid"] == response_database["id_account"]][0],
        "product":
            [product for product in response_product if product["_id"]["$oid"] == response_database["id_product"]][0]
    }
    return response_database_merged


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