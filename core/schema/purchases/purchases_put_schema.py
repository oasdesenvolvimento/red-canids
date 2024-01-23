from typing import Optional, List, Dict
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class PurchasesPut(BaseModel):
    name: Optional[str] = Field(
        default="",
        alias="name",
        title="Name of purchases",
        description="Name of purchases",
        max_length=100,
        examples=["purchases 1"])
    description: Optional[str] = Field(
        default="",
        alias="description",
        title="description of purchases",
        description="Name of purchases",
        max_length=100,
        examples=[" Description purchases 1"])
    id_product: Optional[str] = Field(
        default="",
        alias="id_product",
        title="id of product",
        description="id of product",)
    id_account: Optional[str] = Field(
        default="",
        alias="id_account",
        title="id of account",
        description="id of account",)
    last_account_red_coins: Optional[int] = Field(
        default=0,
        alias="last_account_red_coins",
        title="the last value of red coins",
        description="The last value of red coins of the account before the purchase",
        examples=[3000])
    current_account_red_coins: Optional[int] = Field(
        default=0,
        alias="current_account_red_coins",
        title="current red coins of the account",
        description="current red coins of the account after the purchase",
        examples=[2800])
    total_price: Optional[int] = Field(
        default=0,
        alias="total_price",
        title="total price",
        description="total price of the purchase",
        examples=[200])


class PurchasesPutResponse(BaseModel):
    msg: str = Field(
        default="",
        alias="msg",
        title="Message",
        description="Message",
        examples=["success", "error"])
    data: int = Field(
        default="",
        alias="data",
        title="data",
        description="Response of product")