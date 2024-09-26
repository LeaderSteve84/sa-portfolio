#!/usr/bin/env python3
"""models"""

from flask import current_app
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Text
from datetime import datetime
from typing import Optional
from uuid import uuid4

db = current_app.db


class ProjectDone(db.Model):
    """class of Projects done"""
    __tablename__ = 'projectsDone'
    project_done_id: Mapped[str] = mapped_column(
            String(length=36), primary_key=True, default=lambda: str(uuid4())
    )
    date_created: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    date_updated: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    title: Mapped[str] = mapped_column(String(length=1024))
    project_type: Mapped[str] = mapped_column(String(length=1024))
    description: Mapped[str] = mapped_column(Text)
    stacks: Mapped[str] = mapped_column(String(length=1024))
    role: Mapped[str] = mapped_column(String(length=1024))
    date_cmptd: Mapped[str] = mapped_column(String(length=1024))
    video_link: Mapped[Optional[str]] = mapped_column(
        String(length=2083), unique=False
    )

    def __repr__(self):
        return f'<Project Done {self.title}>'
