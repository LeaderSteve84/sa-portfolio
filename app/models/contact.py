#!/usr/bin/env python3
"""models"""

from flask import current_app
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, DateTime, Text
from datetime import datetime
from uuid import uuid4


db = current_app.db

class ContactMessage(db.Model):
    """class of contact messages"""
    __tablename__ = 'contactMessage'
    message_id: Mapped[str] = mapped_column(
            String(length=36), primary_key=True, default=str(uuid4())
    )
    date_submitted: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )
    name: Mapped[str] = mapped_column(
        String(length=100), unique=False
    )
    email: Mapped[str] = mapped_column(
        String(length=120), unique=False
    )
    subject: Mapped[str] = mapped_column(
        String(length=120), unique=False
    )
    message: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(
        String(length=30), unique=False, default="Unattend"
    )

    def __repr__(self):
        return f'<ContactMessage {self.subject} from {self.name}>'
