#!/usr/bin/env python3
"""models"""

from flask import current_app
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from werkzeug.security import generate_password_hash
from uuid import uuid4

db = current_app.db


class Admin(db.Model):
    """class of Admin table"""
    __tablename__ = 'admin'
    id: Mapped[str] = mapped_column(
        String(length=36), primary_key=True, default=str(uuid4())
    )
    username: Mapped[str] = mapped_column(db.String(length=20), unique=True)
    email: Mapped[str] = mapped_column(db.String(length=30), unique=True)
    password_hash: Mapped[str] = mapped_column(db.String(length=128))
    phone: Mapped[str] = mapped_column(db.String(length=30), unique=True)

    def __repr__(self):
        return f"<admin {self.id}>"

    # password setter
    def set_password(self, password):
        """method to set or change admin password"""
        hash_password = generate_password_hash(password)
        self.password_hash = hash_password
