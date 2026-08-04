# ============================================
# VIDEO MODEL
# ============================================

from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    plan_id = Column(Integer, ForeignKey("plans.id"))
    title = Column(String(200), nullable=False)
    description = Column(Text, default="")
    script = Column(Text, default="")
    status = Column(String(50), default="pending")
    language = Column(String(10), default="en")
    video_path = Column(String(500), default="")
    thumbnail_path = Column(String(500), default="")
    youtube_id = Column(String(50), default="")
    views = Column(Integer, default=0)
    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)
    published_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

    plan = relationship("Plan", backref="videos")
