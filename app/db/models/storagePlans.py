from sqlalchemy import Column, DateTime, Integer,String
from datetime import datetime, timezone

from app.db.base import Base


class StoragePlansModel(Base):
    __tablename__ = "storage_plans"
    id = Column(Integer, primary_key=True, index=True)
    plan_name = Column(String(50), nullable=False)
    storage_limit_gb = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
