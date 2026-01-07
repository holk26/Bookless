from fastapi import APIRouter
from app.api.v1.tenants import router as tenants_router

router = APIRouter()

router.include_router(tenants_router)

@router.get("/health")
def health():
    return {"status": "ok"}
