from sqlalchemy import Column, DateTime, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.db.base import Base

class FilesModel(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    folder_id = Column(Integer, ForeignKey("folders.id"), nullable=False)
    file_name = Column(String(255), nullable=False)
    folder_path = Column(String, nullable=False)
    file_size_gb = Column(Integer, nullable=False)
    file_type = Column(String(50), nullable=False)  # To store file ty  pe like JSON, Docs, Excel, CSV, etc.
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    deleted_at = Column(DateTime, nullable=True)

    # Relationship with the UserModel
    user = relationship("UserModel", backref="files")
    # Relationship with the FoldersModel
    folder = relationship("FoldersModel", backref="files")