from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
import os

router = APIRouter()

@router.get("/")
async def root():
    return {"status": "ok", "message": "Welcome to MaestroBot Web API"}

@router.get("/health")
async def health_check():
    return {"status": "healthy"}

@router.get("/webapp")
async def serve_webapp():
    index_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    return FileResponse(index_path, media_type="text/html")

@router.post("/webapp/feedback")
async def receive_feedback(req: Request):
    data = await req.json()
    print("📩 Feedback dari WebApp:", data)
    return JSONResponse({"status": "received"})
