# db_connect.py
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.connection = None

    async def connect(self):
        try:
            if self.connection is None:
                self.connection = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', 
                      host='azuredoserver.database.windows.net', database='azurevo',
                      user='admin24', password='admin@123')

        except Exception as e:
            print(f"Error: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

# Create an instance of the Database class
db = Database()

# Async functions to connect from the database
async def connect_db():
    await db.connect()

# Async functions to disconnect from the database
async def disconnect_db():
    await db.disconnect()
