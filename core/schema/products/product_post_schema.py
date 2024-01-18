from typing import Optional, List, Dict
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class ProductPost(BaseModel):
    _id: ObjectIdField
    name_product: str = Field(
        default="",
        alias="name_product",
        title="Name of product",
        description="Name of product",
        max_length=100,
        examples=["Product 1"])
    description_product: str = Field(
        default="",
        alias="description_product",
        title="Description of product",
        description="Description of product",
        max_length=300,
        examples=["Description of product 1"])
    price: int = Field(
        default=0,
        alias="price",
        title="Price of product",
        examples=[100],
        description="Points of mission")
    image_product: str = Field(
        default="",
        alias="image_product",
        title="Image of product",
        description="Image of product",
        examples=["https://www.image.com.br"],
        max_length=300)
    date_expiration: str = Field(
        default="",
        alias="date_expiration",
        title="Expiration date of product",
        examples=["2021-01-01 00:00:00"],
        description="Expiration date of product")
    is_enabled: bool = Field(
        default=True,
        alias="is_enabled",
        title="If product is enabled",
        description="If product is enabled")
    stock: int = Field(
        default=0,
        alias="stock",
        title="Stock of product",
        description="Stock of product")
    classification: str = Field(
        default="",
        alias="classification",
        title="Classification of product",
        description="Classification of product, if its normal or rare",
        examples=["normal", "rare"])
    type_product: str = Field(
        default="",
        alias="type_product",
        title="Type of product",
        description="Type of product, if its physical or virtual",
        examples=["physical", "virtual"])
    code_product: Optional[str] = Field(
        default="",
        alias="code_product",
        title="Code of product",
        description="Code of Product")


class ProductPostResponse(BaseModel):
    msg: str = Field(
        default="",
        alias="msg",
        title="Message",
        description="Message",
        examples=["success", "error"])
    data: object = Field(
        default="",
        alias="data",
        title="data",
        description="Response id of mission")
