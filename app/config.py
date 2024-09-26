#!/usr/bin/env python3
"""config module"""
import os
from dotenv import load_dotenv
import logging
from flask import has_request_context, request, current_app
# from werkzeug.security import generate_password_hash

# Load environmental variables from .env file
load_dotenv()


class Config:
    """class for Configurations"""
    FLASK_RUN = os.environ.get('FLASK_APP')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES'))
    JWT_TOKEN_LOCATION = os.environ.get('JWT_TOKEN_LOCATION')  # .split(',')
    JWT_COOKIE_SECURE = os.environ.get('JWT_COOKIE_SECURE')
    JWT_COOKIE_CSRF_PROTECT = os.environ.get('JWT_COOKIE_CSRF_PROTECT')


class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)


# function to create default admin
def create_default_admin():
    """Create a default admin user if it doesn't exist"""
    default_admin_username = os.environ.get('DEFAULT_ADMIN_USERNAME')
    default_admin_email = os.environ.get('DEFAULT_ADMIN_EMAIL')
    default_admin_phone = os.environ.get('DEFAULT_ADMIN_PHONE')
    default_admin_password = os.environ.get('DEFAULT_ADMIN_PASSWORD')

    from app.models import Admin

    # check if username already exist
    admin = Admin.query.filter_by(username=default_admin_username).first()
    if not admin:
        # create an Admin instance
        admin = Admin(
            username=default_admin_username,
            email=default_admin_email,
            password_hash=default_admin_password,
            phone=default_admin_phone
        )
        current_app.logger.info('admin i.e instance of Admin created successfully')
        db = current_app.db
        db.session.add(admin)
        db.session.commit()
        current_app.logger.info(f"Default admin user created: {default_admin_username}")
    current_app.logger.info(f"Default admin {default_admin_username} already exist")
