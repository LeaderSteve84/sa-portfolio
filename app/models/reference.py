#!/usr/bin/env python3
"""models"""

from flask import current_app
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Text
from datetime import datetime
from typing import Optional
from uuid import uuid4

db = current_app.db


class Reference(db.Model):
    """class of Reference"""
    __tablename__ = 'reference'
    reference_id: Mapped[str] = mapped_column(
            String(length=36), primary_key=True, default=lambda: str(uuid4())
    )
    date_created: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    date_updated: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    reference_type: Mapped[str] = mapped_column(
        String(length=50), unique=False
    )
    message: Mapped[str] = mapped_column(Text)
    reference_link: Mapped[Optional[str]] = mapped_column(
        String(length=255), unique=False
    )
    contact: Mapped[Optional[str]] = mapped_column(
        String(length=100), unique=False
    )
    name: Mapped[str] = mapped_column(
        String(length=100), unique=False
    )
    designation: Mapped[str] = mapped_column(
        String(length=50), unique=False
    )

    def __repr__(self):
        return f'<Reference {self.name}>'
