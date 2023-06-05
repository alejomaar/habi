from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware    
from routes.api import api_router
from fastapi import FastAPI

#pipenv run uvicorn app:app --host 0.0.0.0 --port 9797 --reload

app = FastAPI(
    title='HABI Interview'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)