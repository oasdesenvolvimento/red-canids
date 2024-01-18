from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class MissionCompleted(BaseModel):
    id_account: str = Field(
        default="",
        alias="id_account",
        title="Id account of user",
        description="Id account of user",
        max_length=100,
        examples=["123456"])
    id_mission: str = Field(
        default="",
        alias="id_mission",
        title="Id mission completed",
        description="Id mission completed",
        max_length=100,
        examples=["123456"])
    points: int = Field(
        default=0,
        alias="points",
        title="Points of mission",
        description="Points of mission",
        examples=[0])
    type_points: str = Field(
        default="",
        alias="type_points",
        title="Type points of mission",
        description="Type points of mission",
        max_length=100,
        examples=["red_coins"])
    type_mission: str = Field(
        default="",
        alias="type_mission",
        title="Type mission",
        description="Type mission",
        max_length=100,
        examples=[""])


class AccountPost(BaseModel):
    _id: ObjectIdField()
    name: str = Field(
        default="",
        alias="name",
        title="Name of user",
        description="Name of user",
        max_length=100,
        examples=["User 1"])
    email: str = Field(
        default="",
        alias="email",
        title="Email of user",
        description="Email of user",
        max_length=100,
        examples=["teste@mios.pt"])
    password: str = Field(
        default="",
        alias="password",
        title="Password of user",
        description="Password of user",
        max_length=100)
    red_coins: Optional[int] = Field(
        default=0,
        alias="red_coins",
        title="Red coins of user",
        description="Red coins of user",
        examples=[0])
    red_xp: Optional[int] = Field(
        default=0,
        alias="red_xp",
        title="Red xp of user",
        description="Red xp of user",
        examples=[0])
    gmail_access_token: Optional[str] = Field(
        default="",
        alias="gmail_access_token",
        title="Gmail access token of user",
        description="Gmail access token of user",
        max_length=100,
        examples=["123456"])
    apple_access_token: Optional[str] = Field(
        default="",
        alias="apple_access_token",
        title="Apple access token of user",
        description="Apple access token of user",
        max_length=100,
        examples=["123456"])
    facebook_access_token: Optional[str] = Field(
        default="",
        alias="facebook_access_token",
        title="Facebook access token of user",
        description="Facebook access token of user",
        max_length=100,
        examples=["123456"])
    discord_access_token: Optional[str] = Field(
        default="",
        alias="discord_access_token",
        title="Discord access token of user",
        description="Discord access token of user",
        max_length=100,
        examples=["123456"])
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
    code_access: Optional[str] = Field(
        default="",
        alias="code_access",
        title="Code access of user",
        description="Code access of user",
        max_length=6,
        examples=["123456"])
    missions_completed: Optional[List[MissionCompleted]] = Field(
        default=[],
        alias="missions_completed",
        title="Missions completed of user",
        description="Missions completed of user",
        examples=[{
            "id_mission": "123456",
            "date_completed": "2021-01-01 00:00:00",
            "points": 0,
            "type_points": "red_coins"
        }]
    )
