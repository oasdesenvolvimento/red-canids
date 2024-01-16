from typing import Optional, List, Dict
from pydantic import BaseModel, Field


class AdminCreateGetData(BaseModel):
    id: Dict[str, str] = Field(
        alias="_id",
        title="id of admin",
        description="id of admin",
        examples=[{
            "$oid": "5f9d1f9d9c9d6f2e6a9b7f0b"
        }])
    name: str = Field(
        alias="name",
        title="name of admin",
        description="name of admin",
        examples=["Rui Maria"])
    level_access: int = Field(
        alias="level_access",
        title="level access of admin",
        description="lever access of admin(0-normal or 1-supreme)",
        examples=[0])


class AdminCreateGet(BaseModel):
    msg: str = Field(
        alias="msg",
        title="Message of response",
        description="Message of response",
        examples=["Success"])
    data: AdminCreateGetData = Field(
        alias="data",
        title="Data of response",
        description="Data of response",
        examples=[{
            "id": {
                "$oid": "5f9d1f9d9c9d6f2e6a9b7f0b"
            },
            "name": "Rui Maria",
            "level_access": 0
        }])

