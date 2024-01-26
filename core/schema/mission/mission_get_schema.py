from typing import Optional, List, Dict
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class MissionAllGetDataResponse(BaseModel):
    id: Dict[str, str] = Field(
        alias="_id",
        title="Id of mission",
        description="Id of mission",
        examples=[{
                "$oid": "5f9d1f9d9c9d6f2e6a9b7f0b"
            }])
    name_mission: str = Field(
        default="",
        alias="name_mission",
        title="Name of mission",
        description="Name of mission",
        max_length=100,
        examples=["Mission 1"])
    description_mission: str = Field(
        default="",
        alias="description_mission",
        title="Description of mission",
        description="Description of mission",
        max_length=300,
        examples=["Description of mission 1"])
    image_mission: str = Field(
        default="",
        alias="image_mission",
        title="Image of mission",
        description="Image of mission",
        examples=["https://www.image.com.br"])
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
    points: int = Field(
        default=0,
        alias="points",
        title="Points of mission",
        examples=[100],
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
        description="Type of mission, example: video, tik_tok, finder",
        examples=["video"])
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
    videos_mission: Optional[List[str]] = Field(
        default="",
        alias="videos_mission",
        title="Videos of mission",
        description="Videos of mission",
        examples=["https://www.youtube.com/watch?v=123456789"],
        max_length=1000)
    video_source: Optional[str] = Field(
        default="",
        alias="video_source",
        title="Video source of mission",
        description="Video source of mission",
        examples=["youtube"],
        max_length=100)
    code_mission: Optional[str] = Field(
        default="",
        alias="code_mission",
        title="Code of mission",
        description="Code of mission",
        examples=["123456789"],
        max_length=100)
    created_at: str = Field(
        default="",
        alias="created_at",
        title="Created at of mission",
        description="Created at of mission",
        examples=["2021-01-01 00:00:00"])
    updated_at: str = Field(
        default="",
        alias="updated_at",
        title="Updated at of mission",
        description="Updated at of mission",
        examples=["2021-01-01 00:00:00"])


class MissionAllGetResponse(BaseModel):
    msg: str = Field(
        alias="msg",
        title="Message of response",
        description="Message of response",
        examples=["Success"])
    data: List[MissionAllGetDataResponse] = Field(
        alias="data",
        title="Data of response",
        description="Data of response",
        examples=[[{
            "_id": "5f9d1f9d9c9d6f2e6a9b7f0b",
            "name_mission": "Mission 1",
            "description_mission": "Description of mission 1",
            "image_mission": "https://www.image.com.br",
            "expiration_date": "2021-01-01 00:00:00",
            "classification": "normal",
            "points": "100",
            "type_points": "red_coins",
            "type_mission": "youtube",
            "time_mission": "00:00:00",
            "url_mission": "https://www.youtube.com/watch?v=123456789"
        }]])


class MissionGetResponse(BaseModel):
    msg: str = Field(
        alias="msg",
        title="Message of response",
        description="Message of response",
        examples=["Success"])
    data: MissionAllGetDataResponse = Field(
        alias="data",
        title="Data of response",
        description="Data of response",
        examples=[{
            "_id": "5f9d1f9d9c9d6f2e6a9b7f0b",
            "name_mission": "Mission 1",
            "description_mission": "Description of mission 1",
            "image_mission": "https://www.image.com.br",
            "expiration_date": "2021-01-01 00:00:00",
            "classification": "normal",
            "points": "100",
            "type_points": "red_coins",
            "type_mission": "youtube",
            "time_mission": "00:00:00",
            "url_mission": "https://www.youtube.com/watch?v=123456789"
        }])


class MissionValidateToFinderGet(BaseModel):
    msg: str = Field(
        alias="msg",
        title="Message of response",
        description="Message of response",
        examples=["Success"])
    data: bool = Field(
        alias="data",
        title="Data of response",
        description="Data of response",
        examples=[True])
