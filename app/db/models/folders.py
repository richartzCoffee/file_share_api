from sqlalchemy import Column, DateTime, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.db.base import Base

class FoldersModel(Base):
    __tablename__ = "folders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    folder_name = Column(String(255), nullable=False)
    parent_folder_id = Column(Integer, ForeignKey("folders.id"), nullable=False, default=0)  # Self-referential foreign key for subfolders
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    deleted_at = Column(DateTime, nullable=True)

    # Relationship with the UserModel
    user = relationship("UserModel", backref="folders")