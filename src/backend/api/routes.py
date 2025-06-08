from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def ping():
    return {"status": "ok", "message": "StackForge backend running"}
