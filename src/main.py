from fastapi import FastAPI
from src.infrastructure.api.router import router

app = FastAPI()
app.include_router(router)
