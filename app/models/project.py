#!/usr/bin/env python3
"""models"""

from flask import current_app
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Text
from datetime import datetime
from typing import Optional

db = current_app.db

class Project(db.Model):
    """class of Projects done"""
    __tablename__ = 'projects'
    project_id: Mapped[int] = mapped_column(primary_key=True)
    date_created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    date_updated: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    title: Mapped[str] = mapped_column(String(length=1024))
    description: Mapped[str] = mapped_column(Text)
    image_link: Mapped[str] = mapped_column(String(length=1024))
    stacks: Mapped[str] = mapped_column(String(length=1024))
    domain_link: Mapped[Optional[str]] = mapped_column(String(length=1024), unique=False)
    github_link: Mapped[Optional[str]] = mapped_column(String(length=1024), unique=False)
