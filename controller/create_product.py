# create_product.py

from fastapi import HTTPException
from db_connection.db_connect import db

async def create_product(product_data: dict):
    try:
        name = product_data.get("name")
        desc = product_data.get("desc")

        if not name or not desc:
            raise HTTPException(status_code=422, detail="Name and desc are required fields")

        cursor = db.connection.cursor()

        # SQL query to insert a new product
        query = f"INSERT INTO item_details (name, description) VALUES ('{name}', '{desc}')"
        cursor.execute(query)
        db.connection.commit()

        # Get the ID of the newly inserted product
        cursor.execute("SELECT @@IDENTITY AS id")
        new_product_id = cursor.fetchone().id

        # Return the newly created product
        return {"id": new_product_id, "name": name, "desc": desc}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating product: {e}")
