from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .auth import router
from .config import settings

def create_app():
    app = FastAPI()
    app.include_router(router)

    origins = [
        "http://localhost:3000"
    ]
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET,POST,PUT,DELETE"],
        allow_headers=["*"],
    )

    return app
