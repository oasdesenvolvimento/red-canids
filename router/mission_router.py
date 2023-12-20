import json

import core.schema.mission.mission_post_schema
import database

from fastapi import APIRouter, HTTPException
from starlette import status


router = APIRouter()


@router.post("",
             response_model=core.schema.mission.mission_post_schema.MissionPostResponse,
             summary="Create mission",
             response_description="Create mission",
             description="Create mission",
             operation_id="CrateMission")
async def service(values: core.schema.mission.mission_post_schema.MissionPost):
    response = database.mission_database.add_mission(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Admin not created",
            type="error",
            data="Admin not created"
        )))


@router.get("/",
            response_model=core.schema.mission.mission_get_schema.MissionAllGetResponse,
            summary="Return all mission",
            response_description="Return all mission",
            description="Return all mission",
            operation_id="ReturnAllMission")
async def service():
    response = database.mission_database.return_all_mission()
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Admin not created",
            type="error",
            data="Admin not created"
        )))
