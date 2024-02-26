# controller/delete_product.py
from fastapi import HTTPException
from db_connection.db_connect import db

async def delete_product(product_id: int):
    try:
        cursor = db.connection.cursor()

        # Check if the product with the specified id exists
        cursor.execute(f"SELECT * FROM item_details WHERE id = {product_id}")
        existing_product = cursor.fetchone()

        if not existing_product:
            raise HTTPException(status_code=404, detail="Product not found")

        # Delete the product
        cursor.execute(f"DELETE FROM item_details WHERE id = {product_id}")
        db.connection.commit()

        return {"message": "Product deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting product: {e}")