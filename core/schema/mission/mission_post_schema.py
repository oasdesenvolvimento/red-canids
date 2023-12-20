from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class MissionPost(BaseModel):
    _id: ObjectIdField
    name_mission: str = Field(
        default="",
        alias="name_mission",
        title="Name of mission",
        description="Name of mission",
        max_length=100,
        examples=["Mission 1"],
        pattern="^[a-zA-Z0-9_ ]*$")
    description_mission: str = Field(
        default="",
        alias="description_mission",
        title="Description of mission",
        description="Description of mission",
        max_length=300,
        examples=["Description of mission 1"],
        pattern="^[a-zA-Z0-9_ ]*$")
    image_mission: str = Field(
        default="",
        alias="image_mission",
        title="Image of mission",
        description="Image of mission",
        examples=["https://www.image.com.br"],
        max_length=300)
    expiration_date: str = Field(
        default="",
        alias="expiration_date",
        title="Expiration date of mission",
        examples=["2021-01-01 00:00:00"],
        description="Expiration date of mission")
    classification: str = Field(
        default="",
        alias="classification",
        title="Classification of mission",
        description="Classification of mission, example: rare, normal",
        examples=["normal"])
    points: str = Field(
        default="",
        alias="points",
        title="Points of mission",
        examples=["100"],
        description="Points of mission")
    type_points: str = Field(
        default="",
        alias="type_points",
        title="Type points of mission",
        description="Type points of mission, example: red_coins, red_xp",
        examples=["red_coins"])
    type_mission: str = Field(
        default="",
        alias="type_mission",
        title="Type of mission",
        description="Type of mission, example: youtube, tik_tok, finder",
        examples=["youtube"])
    time_mission: Optional[str] = Field(
        default="",
        alias="time_mission",
        title="Time of mission",
        examples=["00:00:00"],
        description="If type mission is one video, this field is required")
    url_mission: Optional[str] = Field(
        default="",
        alias="url_mission",
        title="Url of mission",
        description="Url of mission",
        examples=["https://www.youtube.com/watch?v=123456789"],
        max_length=300)
    code_mission: str = Field(
        default="",
        alias="code_mission",
        title="Code of mission",
        description="Code of mission",
        examples=["123456789"],
        max_length=100)


class MissionPostResponse(BaseModel):
    msg: str = Field(
        default="",
        alias="msg",
        title="Message",
        description="Message",
        examples=["success", "error"])
    data_type: str = Field(
        default="",
        alias="data_type",
        title="Type of data",
        description="Type of data",
        examples=["text", "json"])
    data: object = Field(
        default="",
        alias="data",
        title="data",
        description="Response id of mission")
