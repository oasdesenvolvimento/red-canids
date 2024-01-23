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
            msg="Error to return missions",
            type="error",
            data="Error to return missions"
        )))


@router.get("/{id_mission}",
            response_model=core.schema.mission.mission_get_schema.MissionGetResponse,
            summary="Return mission by id",
            response_description="Return mission by id",
            description="Return mission by id",
            operation_id="ReturnMissionById")
async def service(id_mission: str):
    response = database.mission_database.return_mission_by_id(id_mission)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Error to return mission",
            type="error",
            data="Error to return mission"
        )))


@router.get("/validate-mission-finder/{id_mission}/{code}",
            response_model=core.schema.mission.mission_get_schema.MissionValidateToFinderGet,
            summary="Validate mission finder",
            response_description="Validate mission finder",
            description="Validate mission finder",
            operation_id="ValidateMissionFinder")
async def service(id_mission: str, code: str):
    response = database.mission_database.validate_mission_finder(id_mission, code)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Error to validate mission finder",
            type="error",
            data="Error to validate mission finder"
        )))


@router.put("/update-mission",
            response_model=core.schema.mission.mission_put_schema.MissionPutResponse,
            summary="Update mission",
            response_description="Update mission",
            description="Update mission by id",
            operation_id="UpdateMissionById")
async def service(id_mission: str, value: core.schema.mission_put_schema.MissionPut):
    response = database.mission_database.update_mission_by_id(id_mission, value)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Error to update mission",
            type="error",
            data="Error to update mission"
        )))


@router.delete("/delete-mission/{id_mission}",
               response_model=core.schema.mission.mission_put_schema.MissionPutResponse,
               summary="Delete mission",
               response_description="Delete mission",
               description="Delete mission by id",
               operation_id="DeleteMissionById")
async def service(id_mission: str):
    response = database.mission_database.delete_mission_by_id(id_mission)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Error to delete mission",
            type="error",
            data="Error to delete mission"
        )))