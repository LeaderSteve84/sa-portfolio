#!/usr/bin/env python3
"""models"""

from flask import current_app
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Text
from datetime import datetime
from typing import Optional
from uuid import uuid4

db = current_app.db


class Writing(db.Model):
    """class of Technical writings done"""
    __tablename__ = 'writings'
    writing_id: Mapped[str] = mapped_column(
            String(length=36), primary_key=True, default=lambda: str(uuid4())
    )
    date_created: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    date_updated: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    title: Mapped[str] = mapped_column(String(length=1024))
    image_link: Mapped[Optional[str]] = mapped_column(
        String(length=2083), unique=False
    )
    description: Mapped[str] = mapped_column(Text)
    published_link: Mapped[Optional[str]] = mapped_column(
        String(length=2083), unique=False
    )

    def __repr__(self):
        return f"<Technical Writing {self.title}>"
