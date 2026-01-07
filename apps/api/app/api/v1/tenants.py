from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError

from app.db.session import SessionLocal
from app.db.models.tenant import Tenant

router = APIRouter(prefix="/tenants", tags=["tenants"])

class TenantCreate(BaseModel):
    name: str
    slug: str

class TenantResponse(BaseModel):
    id: str
    name: str
    slug: str
    is_active: bool

    class Config:
        from_attributes = True

@router.post("", response_model=TenantResponse)
def create_tenant(payload: TenantCreate):
    db = SessionLocal()
    tenant = Tenant(
        name=payload.name,
        slug=payload.slug,
    )
    try:
        db.add(tenant)
        db.commit()
        db.refresh(tenant)
        return tenant
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Tenant slug already exists")
    finally:
        db.close()
