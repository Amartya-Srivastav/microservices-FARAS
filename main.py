# main.py
from fastapi import FastAPI
from db_connection.db_connect import db, connect_db, disconnect_db
from routes.routes import router as main_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# On startup, connect to the database
@app.on_event("startup")
async def startup_db_client():
    await connect_db()

# On shutdown, disconnect from the database
@app.on_event("shutdown")
async def shutdown_db_client():
    await disconnect_db()

# Allowing CORS Policy
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

# Include routes from the route file
app.include_router(main_router)