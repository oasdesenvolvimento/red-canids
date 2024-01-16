from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class AdminPost(BaseModel):
    _id: ObjectIdField()
    name: str = Field(
        default="",
        alias="name",
        title="name of admin",
        description="name of admin",
        examples=["Rui Maria"])
    email: str = Field(
        default="",
        alias="email",
        title="email of admin",
        description="email of admin",
        examples=["email@gmail.com"])
    password: str = Field(
        default="",
        alias="password",
        title="Password of admin",
        description="Password of admin",
        max_length=100)
    level_access: int = Field(
        default=0,
        alias="level_access",
        title="level access of admin",
        description="level access of admin",
        examples=[0]
    )