from typing import Optional, List
from mongoengine import ObjectIdField
from pydantic import BaseModel, Field


class ImagePostResponseData(BaseModel):
    name: str = Field(
        default="",
        alias="name",
        title="Name of image",
        description="Name of image",
        examples=["Image 1"])
    type: str = Field(
        default="",
        alias="type",
        title="Type of image",
        description="Type of image",
        examples=["image/png"])
    url: str = Field(
        default="",
        alias="url",
        title="Url of image",
        description="Url of image",
        max_length=300,
        examples=["https://www.image.com.br"]
    )


class ImagePostResponse(BaseModel):
    files: List[ImagePostResponseData] = Field(
        alias="files",
        title="Files",
        description="Files",
        examples=[{
            "name": "Image 1",
            "type": "image/png",
            "url": "https://www.image.com.br"
        }]
    )