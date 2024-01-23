import json

import core.schema.purchases.purchases_post_schema as PostSchema
import core.schema.purchases.purchases_get_schema as GetSchema
import core.schema.purchases.purchases_put_schema as PutSchema
import database

from fastapi import APIRouter, HTTPException
from starlette import status


router = APIRouter()


@router.post("",
             response_model=PostSchema.PurchasesPostResponse,
             summary="Create purchase",
             response_description="Create purchase",
             description="Create purchase",
             operation_id="CreatePurchase")
async def service(value: PostSchema.PurchasesPost):
    response = database.purchases_database.add_purchases(value)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Purchase not created",
            type="error",
            data="Purchase not created"
        )))


@router.get("",
            response_model=GetSchema.PurchaseAllGetResponse,
            summary="Return all purchase",
            response_description="Return all purchase",
            description="Return all purchase",
            operation_id="ReturnAllPurchase")
async def service():
    response = database.purchases_database.return_all_purchases()
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Error to return purchases",
            type="error",
            data="Error to return purchases"
        )))


@router.get("/{id_purchase}",
            response_model=GetSchema.PurchaseGetResponse,
            summary="Return purchase by id",
            response_description="Return purchase by id",
            description="Return purchase by id",
            operation_id="ReturnPurchaseById")
async def service(id_purchase: str):
    response = database.purchases_database.return_purchase_by_id(id_purchase)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Error to return purchase",
            type="error",
            data="Error to return purchase"
        )))


@router.put("/update-purchase",
            response_model=PutSchema.PurchasesPutResponse,
            summary="Update purchase by id",
            response_description="Update purchase by id",
            description="Update purchase by id",
            operation_id="UpdatePurchaseById")
async def service(id_purchase: str, value: PutSchema.PurchasesPut):
    response = database.purchases_database.update_purchase_by_id(id_purchase, value)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Purchase not updated",
            type="error",
            data="Purchase not updated"
        )))


@router.put("/update-purchase/done",
            response_model=PutSchema.PurchasesPutResponse,
            summary="Update purchase done by id",
            response_description="Update purchase done by id",
            description="Update purchase done by id",
            operation_id="UpdatePurchaseDoneVisibleById")
async def service(id_purchase: str):
    response = database.purchases_database.update_purchase_done_visible(id_purchase)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Purchase not updated",
            type="error",
            data="Purchase not updated"
        )))


@router.delete("/{id_purchase}",
               response_model=PutSchema.PurchasesPutResponse,
               summary="Delete purchase by id",
               response_description="Delete purchase by id",
               description="Delete purchase by id",
               operation_id="DeletePurchaseById")
async def service(id_purchase: str):
    response = database.purchases_database.delete_purchase_by_id(id_purchase)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Purchase not deleted",
            type="error",
            data="Purchase not deleted"
        )))
