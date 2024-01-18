import json

import core.schema.products.product_post_schema as PostSchema
import core.schema.products.product_get_schema as GetSchema
import core.schema.products.product_put_schema as PutSchema
import database

from fastapi import APIRouter, HTTPException
from starlette import status


router = APIRouter()


@router.post("",
             response_model=PostSchema.ProductPostResponse,
             summary="Create product",
             response_description="Create product",
             description="Create product",
             operation_id="CreateProduct")
async def service(values: PostSchema.ProductPost):
    response = database.products_database.add_product(values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Product not created",
            type="error",
            data="Product not created"
        )))


@router.get("/",
            response_model=GetSchema.ProductAllGetResponse,
            summary="Return all products",
            response_description="Return all products",
            description="Return all products",
            operation_id="ReturnAllProducts")
async def service():
    response = database.products_database.return_all_product()
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Error to return products",
            type="error",
            data="Error to return products"
        )))


@router.get("/{id_product}",
            response_model=GetSchema.ProductGetResponse,
            summary="Return product by id",
            response_description="Return product by id",
            description="Return product by id",
            operation_id="ReturnProductById")
async def service(id_product: str):
    response = database.products_database.return_product_by_id(id_product)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Error to return product",
            type="error",
            data="Error to return product"
        )))


@router.put("/update-product",
            response_model=PutSchema.ProductPutResponse,
            summary="Update product by id",
            response_description="Update product by id",
            description="Update product by id",
            operation_id="UpdateProductById")
async def service(id_product: str, values: PutSchema.ProductPut):
    response = database.products_database.update_product_by_id(id_product, values)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Product not updated",
            type="error",
            data="Product not updated"
        )))


@router.delete("/{id_product}",
               response_model=PutSchema.ProductPutResponse,
               summary="Delete product by id",
               response_description="Delete product by id",
               description="Delete product by id",
               operation_id="DeleteProductById")
async def service(id_product: str):
    response = database.products_database.delete_product_by_id(id_product)
    if response is not None:
        return {"msg": "success", "data": response}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=json.dumps(dict(
            msg="Product not deleted",
            type="error",
            data="Product not deleted"
        )))
