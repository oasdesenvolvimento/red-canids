from typing import Optional, List, Dict
from pydantic import BaseModel, Field


class AccountCreateGetData(BaseModel):
    id: Dict[str, str] = Field(
        alias="_id",
        title="Id of user",
        description="Id of user",
        examples=[{
                "$oid": "5f9d1f9d9c9d6f2e6a9b7f0b"
            }])
    code_access: str = Field(
        alias="code_access",
        title="Code access of user",
        description="Code access of user",
        max_length=100,
        examples=["123456"],
        pattern="^[a-zA-Z0-9_ ]*$")


class AccountCreateGet(BaseModel):
    msg: str = Field(
        alias="msg",
        title="Message of response",
        description="Message of response",
        examples=["Success"])
    data: AccountCreateGetData = Field(
        alias="data",
        title="Data of response",
        description="Data of response",
        examples=[{
            "id": {
                "$oid": "5f9d1f9d9c9d6f2e6a9b7f0b"
            },
            "code_access": "123456"
        }])