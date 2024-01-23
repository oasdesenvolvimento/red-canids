from typing import Optional, List, Dict
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class PurchaseAllGetDataResponse(BaseModel):
    id: Dict[str, str] = Field(
        alias="_id",
        title="Id of product",
        description="Id of product",
        examples=[{
            "$oid": "5f9d1f9d9c9d6f2e6a9b7f0b"
        }])
    name: str = Field(
        default="",
        alias="name",
        title="Name of purchases",
        description="Name of purchases",
        max_length=100,
        examples=["purchases 1"])
    description: str = Field(
        default="",
        alias="description",
        title="description of purchases",
        description="Name of purchases",
        max_length=100,
        examples=[" Description purchases 1"])
    id_product: str = Field(
        default="",
        alias="id_product",
        title="id of product",
        description="id of product",)
    id_account: str = Field(
        default="",
        alias="id_account",
        title="id of account",
        description="id of account",)
    last_account_red_coins: int = Field(
        default=0,
        alias="last_account_red_coins",
        title="the last value of red coins",
        description="The last value of red coins of the account before the purchase",
        examples=[3000])
    current_account_red_coins: int = Field(
        default=0,
        alias="current_account_red_coins",
        title="current red coins of the account",
        description="current red coins of the account after the purchase",
        examples=[2800])
    total_price: int = Field(
        default=0,
        alias="total_price",
        title="total price",
        description="total price of the purchase",
        examples=[200])
    is_visible: bool = Field(
        alias="is_visible",
        title="is purchase visible",
    )
    is_done: bool = Field(
        alias="is_done",
        title="is purchase done",
    )
    created_at: str = Field(
        alias="created_at"
    )
    updated_at: str = Field(
        alias="updated_at"
    )


class PurchaseAccount(BaseModel):
    id: Dict[str, str] = Field(
        alias="_id",
        title="Id of product",
        description="Id of product",
        examples=[{
            "$oid": "5f9d1f9d9c9d6f2e6a9b7f0b"
        }])
    name: str = Field(
        default="",
        alias="name",
        title="Name of product",
        description="Name of product",
        max_length=100,
        examples=["Teste"])
    email: str = Field(
        default="",
        alias="email",
        title="Email of user",
        description="Email of user",
        max_length=100,
        examples=["test@teste.com"])


class PurchaseProduct(BaseModel):
    id: Dict[str, str] = Field(
        alias="_id",
        title="Id of product",
        description="Id of product",
        examples=[{
            "$oid": "5f9d1f9d9c9d6f2e6a9b7f0b"
        }])
    name_product: str = Field(
        default="",
        alias="name_product",
        title="Name of product",
        description="Name of product",
        max_length=100,
        examples=["Teste"])
    description_product: str = Field(
        default="",
        alias="description_product",
        title="Description of product",
        description="Description of product",
        max_length=100,
        examples=["Teste"])
    image_product: str = Field(
        default="",
        alias="image_product",
        title="Image of product",
        description="Image of product",
        max_length=100,
        examples=["Teste"])


class PurchaseAllGetResponseEmbedded(BaseModel):
    purchase: PurchaseAllGetDataResponse
    account: PurchaseAccount
    product: PurchaseProduct


class PurchaseAllGetResponse(BaseModel):
    msg: str = Field(
        alias="msg",
        title="Message of response",
        description="Message of response",
        examples=["Success"])
    data: List[PurchaseAllGetResponseEmbedded] = Field(
        alias="data",
        title="Data of response",
        description="Data of response")


class PurchaseGetResponse(BaseModel):
    msg: str = Field(
        alias="msg",
        title="Message of response",
        description="Message of response",
        examples=["Success"])
    data: PurchaseAllGetDataResponse = Field(
        alias="data",
        title="Data of response",
        description="Data of response",
        examples=[[{
            "_id": {"$oid": "123124323894723984"},
            "name": "",
            "description": "",
            "id_product": "",
            "id_account": "",
            "last_account_red_coins": 0,
            "current_account_red_coins": 0,
            "total_price": 0,
            "is_visible": True,
            "is_done": False,
            "created_at": "",
            "updated_at": ""
        }]])