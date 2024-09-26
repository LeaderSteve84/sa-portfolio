#!/usr/bin/env python3
"""models"""

from flask import current_app
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Text
from datetime import datetime
from typing import Optional
from uuid import uuid4

db = current_app.db

class FeaturedProject(db.Model):
    """class of Projects done"""
    __tablename__ = 'featured_projects'
    featured_project_id: Mapped[str] = mapped_column(
        String(length=36), primary_key=True, default=str(uuid4())
    )
    date_created: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    date_updated: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    title: Mapped[str] = mapped_column(String(length=1024))
    description: Mapped[str] = mapped_column(Text)
    image_link: Mapped[Optional[str]] = mapped_column(
        String(length=2083), unique=False
    )
    stacks: Mapped[str] = mapped_column(String(length=1024))
    role: Mapped[Optional[str]] = mapped_column(
        Text, unique=False
    ) 
    challenges: Mapped[Optional[str]] = mapped_column(
        Text, unique=False
    )
    date_cmptd: Mapped[Optional[str]] = mapped_column(
        String(length=1024), unique=False
    )
    domain_link: Mapped[Optional[str]] = mapped_column(
        String(length=2083), unique=False
    )
    github_link: Mapped[Optional[str]] = mapped_column(
        String(length=2083), unique=False
    )
    video_link: Mapped[Optional[str]] = mapped_column(
        String(length=2083), unique=False
    )

    def __repr__(self):
        return f'<Project {self.title}>'
