from fastapi import APIRouter

router = APIRouter

async def root():
    return {"Message": "Hello World"}