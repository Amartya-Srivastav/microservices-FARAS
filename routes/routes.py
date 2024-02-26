# route.py
from fastapi import APIRouter
from fastapi import HTTPException

# importing all controller
from controller.server_check import root
from controller.get_products import get_products
from controller.create_product import create_product
from controller.update_product import update_product
from controller.delete_product import delete_product

router = APIRouter()

# importing all logics
@router.get("/home")
async def root_route():
    return await root()

@router.get("/getProducts")
async def get_products_route():
    return await get_products()

@router.post("/create-product")
async def create_product_route(product_data: dict):
    return await create_product(product_data)

@router.put("/update-product/{product_id}")
async def update_product_route(product_id: int, product_data: dict):
    return await update_product(product_id, product_data.get("name"), product_data.get("desc"))

@router.delete("/delete-product/{product_id}")
async def delete_product_route(product_id: int):
    return await delete_product(product_id)