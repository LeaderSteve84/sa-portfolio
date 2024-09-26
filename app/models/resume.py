#!/usr/bin/env python3
"""models"""

from flask import current_app
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime
from datetime import datetime
from typing import Optional
from uuid import uuid4

db = current_app.db


class Resume(db.Model):
    """class of Reference"""
    __tablename__ = 'resume'
    resume_id: Mapped[str] = mapped_column(
        String(length=36), primary_key=True, default=str(uuid4())
    )
    date_created: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    date_updated: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    resume_image1_link: Mapped[Optional[str]] = mapped_column(
        String(length=255), unique=False
    )
    resume_image2_link: Mapped[Optional[str]] = mapped_column(
        String(length=255), unique=False
    )
    resume_image3_link: Mapped[Optional[str]] = mapped_column(
        String(length=255), unique=False
    )
    resume_image4_link: Mapped[Optional[str]] = mapped_column(
        String(length=255), unique=False
    )
    resume_download_link: Mapped[Optional[str]] = mapped_column(
        String(length=255), unique=False
    )

    def __repr__(self):
        return f'<Resume {self.resume_id}>'
