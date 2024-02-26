# get_products.py
from fastapi import APIRouter, HTTPException
from db_connection.db_connect import db
from model.db_model import Product

router = APIRouter()

async def get_products():
    try:
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM item_details")
        data = cursor.fetchall()

        # Convert data to a list of dictionaries
        result = []
        for row in data:
            result.append(dict(zip([column[0] for column in cursor.description], row)))

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching items: {e}")
