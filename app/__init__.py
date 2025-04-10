#!/usr/bin/env python3
"""app package init"""

from flask import Flask, render_template
from flask_mail import Mail, Message
from app.config import RequestFormatter
import logging
# from logging.handlers import RotatingFileHandler
from logging.handlers import SMTPHandler
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect
from flask_caching import Cache
from .config import cache_config
from supabase import create-client
import os

# configuration logging before app creation,
# for stream, file and mail handlers.
logger = logging.getLogger()
formatter = RequestFormatter(
    '[%(asctime)s] %(remote_addr)s requested %(url)s \
    %(levelname)s in %(module)s: %(message)s'
)
logger.setLevel(logging.DEBUG)

# add stream handler to the root logger
streamHandler = logging.StreamHandler()
streamHandler.setLevel(logging.DEBUG)
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# add file handler to the root logger
# maxBytes is 50MB size

# fileHandler = RotatingFileHandler(
#    'my-portfolio.log', backupCount=10, maxBytes=52428800
# )
# fileHandler.setLevel(logging.DEBUG)
# fileHandler.setFormatter(formatter)
# logger.addHandler(fileHandler)

# create the base class
class Base(DeclarativeBase):
    pass


# create the db instance
db = SQLAlchemy(model_class=Base)
migrate = Migrate()

# Create the jwt instance
jwt = JWTManager()


# create instance of CSRFProtect
csrf = CSRFProtect()


def create_app():
    """function to create flask app"""
    app = Flask(__name__)

    # set configuration into app
    app.config.from_object('app.config.Config')
    app.config.from_mapping(cache_config)

    # Initialize mail instance
    mail = Mail(app)
    app.mail = mail  # set mail into app context

    # create db instance
    db.init_app(app)
    app.db = db  # set db into app context
    migrate.init_app(app, db)

    # Initialize JWT Manager
    jwt.init_app(app)
    app.jwt = jwt
    
    # Supabase client for database access
    supabase = create_client(
        os.environ.get("SUPABASE_URL"),
        os.environ.get("SUPABASE_KEY")
    )

    # initialize CSRFProtect instance
    csrf.init_app(app)
    app.csrf = csrf

    # Initialize the Cache instance
    cache = Cache(app)
    app.cache = cache

    # create SMTP handler and added to the root logger
    if not app.debug:
        try:
            mail_handler = SMTPHandler(
                mailhost=(
                    app.config['MAIL_SERVER'],
                    app.config['MAIL_PORT']
                ),
                fromaddr=app.config['MAIL_DEFAULT_SENDER'],
                toaddrs=['steveadahson@gmail.com'],
                subject='System error - log',
                credentials=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']),
                timeout=30
            )
            mail_handler.setLevel(logging.ERROR)
            mail_handler.setFormatter(formatter)
            app.logger.addHandler(mail_handler)
        except Exception as e:
            app.logger.error(f"Failed to set up email logging: {e}")

    with app.app_context():
        # import all the models from app/models/__init__.py
        from app.models import Admin, FeaturedProject, ProjectDone, \
            Writing, Reference, Resume, ContactMessage

        @app.errorhandler(404)
        def page_not_found(e):
            return render_template('page_not_found.html'), 404

        @app.errorhandler(500)
        def internal_server_error(e):
            return render_template('int_serv_error.html'), 500

        # db.drop_all() 
        # create all tables in database
        db.create_all()
        app.logger.info("DB Tables created successfully")

        from app.config import create_default_admin
        create_default_admin()
        app.logger.info("Default Admin created successfully")

        # import main blueprint
        from app.routes import bp

        # register main blueprint to app
        app.register_blueprint(bp)

        # import after request
        from app.routes.afterRequest import refresh_expiring_jwts

        # register after_request
        app.after_request(refresh_expiring_jwts)

    return app
