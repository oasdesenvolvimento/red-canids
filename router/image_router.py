import json
import uuid
import base64

import core.schema.image.image_post_schema
import internal

from fastapi import APIRouter, HTTPException, UploadFile, File
from starlette import status

router = APIRouter()


@router.post("/add-image",
             response_model=core.schema.image.image_post_schema.ImagePostResponse,
             name="Add image in project",
             summary="Add image in project",
             description="Add image in project",
             operation_id="AddImageInProject")
async def service(file: UploadFile = File(...)):
    """
    Add image ion storage
    :param file:
    :return: json
    """
    if file:
        file_contents = await file.read()

        id_image = str(uuid.uuid4())

        image_base64 = base64.b64encode(file_contents).decode("utf-8")

        response = internal.save_image_in_storage.upload_image(image_base64, id_image)

        return {"files": [{"name": file.filename, "type": file.content_type, "url": response}]}
    else:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Image not added",
            type="error",
            data="Image not added"
        )))
