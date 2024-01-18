import json
import datetime
import core.model as model


def add_product(values):
    response = model.products_model.Product(
        name_product=values.name_product,
        description_product=values.description_product,
        price=values.price,
        image_product=values.image_product,
        date_expiration=values.date_expiration,
        is_enabled=values.is_enabled,
        stock=values.stock,
        classification=values.classification,
        type_product=values.type_product,
        code_product=values.code_product,
        created_at=str(datetime.datetime.now()),
        updated_at=str(datetime.datetime.now())
    ).save()
    return str(response.auto_id_0)


def return_all_product():
    response_database = model.products_model.Product.objects().to_json()
    response_database = json.loads(response_database)
    return response_database


def return_product_by_id(id_product):
    response_database = model.products_model.Product.objects(_id=id_product).first().to_json()
    response_database = json.loads(response_database)
    return response_database


def update_product_by_id(id_product, values):
    response_database = model.products_model.Product.objects(_id=id_product).update_one(
        name_product=values.name_product,
        description_product=values.description_product,
        price=values.price,
        image_product=values.image_product,
        date_expiration=values.date_expiration,
        is_enabled=values.is_enabled,
        stock=values.stock,
        classification=values.classification,
        type_product=values.type_product,
        code_product=values.code_product,
        updated_at=str(datetime.datetime.now())
    )
    return response_database


def delete_product_by_id(id_product):
    response_database = model.products_model.Product.objects(_id=id_product)
    response = response_database.delete()
    return response