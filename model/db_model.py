# db_model.py
from redis_om import HashModel
from db_connection.db_connect import db

class Product(HashModel):
    id: int
    name: float
    desc: int

    class Meta:
        database=db.connect()