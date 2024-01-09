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
