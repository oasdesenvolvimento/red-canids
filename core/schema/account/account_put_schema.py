from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class AccountPut(BaseModel):
    name: Optional[str] = Field(
        default="",
        alias="name",
        title="Name of user",
        description="Name of user",
        max_length=100,
        examples=["User 1"])
    email: Optional[str] = Field(
        default="",
        alias="email",
        title="Email of user",
        description="Email of user",
        max_length=100,
        examples=["teste@mios.pt"])
    genre: Optional[str] = Field(
        default="",
        alias="genre",
        title="genre of user",
        description="genre of user",
        examples=["Não Binario"])
    background_photo: Optional[str] = Field(
        default="",
        alias="background_photo",
        title="background photo of user",
        description="background photo of user")
    twitter_access_token: Optional[str] = Field(
        default="",
        alias="twitter_access_token",
        title="Twitter access token of user",
        description="Twitter access token of user",
        max_length=100,
        examples=["123456"])
    photo_profile: Optional[str] = Field(
        default="",
        alias="photo_profile",
        title="Photo profile of user",
        description="Photo profile of user",
        max_length=100,
        examples=["https://www.image.com.br"])
    birthday: Optional[str] = Field(
        default="",
        alias="birthday",
        title="Birthday of user",
        description="Birthday of user",
        max_length=100,
        examples=["2021-01-01 00:00:00"])
    bio: Optional[str] = Field(
        default="",
        alias="bio",
        title="Bio of user",
        description="Bio of user",
        max_length=5000,
        examples=["Bio of user"])


class AccountPutResponse(BaseModel):
    msg: str = Field(
        alias="msg",
        title="Message of response",
        description="Message of response",
        examples=["Success"])
    data: object = Field(
        alias="data",
        title="Data of response",
        description="Data of response"
    )