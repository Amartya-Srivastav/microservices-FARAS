# controller/update_products.py
from fastapi import HTTPException
from db_connection.db_connect import db

async def update_product(product_id: int, name: str, desc: str):
    try:
        cursor = db.connection.cursor()

        # Check if the product with the specified id exists
        cursor.execute(f"SELECT * FROM item_details WHERE id = {product_id}")
        existing_product = cursor.fetchone()

        if not existing_product:
            raise HTTPException(status_code=404, detail="Product not found")

        # Update the name and description
        cursor.execute(
            f"UPDATE item_details SET name = '{name}', description = '{desc}' WHERE id = {product_id}"
        )
        db.connection.commit()

        return {"id": product_id, "name": name, "desc": desc}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating product: {e}")