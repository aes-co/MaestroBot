from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from web_app_backend.routes import router

app = FastAPI(
    title="MaestroBot WebApp API",
    description="Backend for MaestroBot Web Interface",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
