from fastapi import FastAPI
from app.api.routes.blob import router as blob_router

app = FastAPI()

app.include_router(blob_router, prefix="/blob")