import json
import database
import core.schema.admin_account as schema

from fastapi import APIRouter, HTTPException
from starlette import status


router = APIRouter()


@router.post("",
             response_model=schema.admin_account_get_schema.AdminCreateGet,
             summary="Create Admin",
             response_description="Create Admin",
             description="Create Admin",
             operation_id="CreateAdmin")
async def service(values: schema.admin_account_post_schema.AdminPost):
    response = database.admin_database.add_new_admin(values)
    if response == 401:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=json.dumps(dict(
            msg="Email already registered",
            type="error",
            data="Email already registered"
        )))
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Admin not created",
            type="error",
            data="Admin not created"
        )))


@router.get("/{email}/{password}",
            response_model=schema.admin_account_get_schema.AdminLoginGet,
            summary="Return admin by email and password",
            response_description="Return admin by email and password",
            description="Return admin by email and password",
            operation_id="ReturnAdminByLogin")
async def service(email: str, password: str):
    """
    Return admin by email and password
    :param email:
    :param password:
    :return:
    """
    response = database.admin_database.return_admin_by_login(email, password)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Admin not found",
            type="error",
            data="Admin not found"
        )))