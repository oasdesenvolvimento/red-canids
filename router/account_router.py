import json
import database
import core.schema.account.account_post_schema

from fastapi import APIRouter, HTTPException
from starlette import status


router = APIRouter()


@router.post("",
             response_model=core.schema.account_get_schema.AccountCreateGet,
             summary="Create account",
             response_description="Create account",
             description="Create account",
             operation_id="CreateAccount")
async def service(values: core.schema.account_post_schema.AccountPost):
    response = database.account_database.add_new_account(values)
    if response is not None:
        database.account_database.add_red_xp_some(values.apple_access_token, 100)
    if response == 401:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=json.dumps(dict(
            msg="Email already registered",
            type="error",
            data="Email already registered"
        )))
    if response is not None:
        return {"msg": "success", "data": {
            "_id": {
                "$oid": response["_id"]
            },
            "code_access": response["code_access"]
        }}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Admin not created",
            type="error",
            data="Admin not created"
        )))


@router.get("",
            response_model=core.schema.account_get_schema.AccountAllGet,
            summary="Return all account",
            response_description="Return all account",
            description="Return all account",
            operation_id="ReturnAllAccount")
async def service():
    response = database.account_database.return_all_account()
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Admin not created",
            type="error",
            data="Admin not created"
        )))


@router.get("/{email}/{code_access}",
            response_model=core.schema.account_get_schema.AccountGet,
            summary="Return account by email and code access",
            response_description="Return account by email and code access",
            description="Return account by email and code access",
            operation_id="ReturnAccountByEmailAndCodeAccess")
async def service(email: str, code_access: str):
    response = database.account_database.return_account_by_email_and_code_access(email, code_access)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="User not found",
            type="error",
            data="User not found"
        )))


@router.put("/mission/completed/",
            response_model=core.schema.account_get_schema.AccountGet,
            summary="Update mission completed",
            response_description="Update mission completed",
            description="Update mission completed",
            operation_id="UpdateMissionCompleted")
async def service(values: core.schema.account_post_schema.MissionCompleted):
    response = database.account_database.update_mission_completed(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Error to update mission completed",
            type="error",
            data="Error to update mission completed"
        )))


@router.get("/mission/check-if-already-completed/{id_account}/{id_mission}",
            response_model=core.schema.account_get_schema.AccountGet,
            summary="Check if mission already completed",
            response_description="Check if mission already completed",
            description="Check if mission already completed",
            operation_id="CheckIfMissionAlreadyCompleted")
async def service(id_account: str, id_mission: str):
    response = database.account_database.check_if_mission_already_completed(id_account, id_mission)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="User not found",
            type="error",
            data="User not found"
        )))


@router.put("/add-red-coins",
            response_model=core.schema.account_get_schema.AccountGet,
            summary="Add Red coins to account",
            response_description="Add Red coins to account",
            description="Add Red coins to account",
            operation_id="AddRedCoins")
async def service(id_account: str, red_coins: int):
    response = database.account_database.add_red_coins(id_account, red_coins)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="User not found",
            type="error",
            data="User not found"
        )))


@router.put("/add-red-xp",
            response_model=core.schema.account_get_schema.AccountGet,
            summary="Add Red xp to account",
            response_description="Add Red xp to account",
            description="Add Red xp to account",
            operation_id="AddRedXp")
async def service(id_account: str, red_xp: int):
    response = database.account_database.add_red_xp(id_account, red_xp)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="User not found",
            type="error",
            data="User not found"
        )))