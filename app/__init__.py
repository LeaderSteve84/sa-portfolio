#!/usr/bin/env python3
"""app package init"""

from flask import Flask
from flask_mail import Mail, Message
from app.config import RequestFormatter
import logging
from logging.handlers import RotatingFileHandler
from logging.handlers import SMTPHandler
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect

# Initialize mail instance globally
mail = Mail()

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
fileHandler = RotatingFileHandler(
    'my-portfolio.log', backupCount=10, maxBytes=52428800
)
fileHandler.setLevel(logging.DEBUG)
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

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

    mail.init_app(app)
    app.mail = mail  # set mail into app context

    # set configuration into app
    app.config.from_object('app.config.Config')
    
    # create db instance
    db.init_app(app)
    app.db = db  # set db into app context
    migrate.init_app(app, db)

    # Initialize JWT Manager
    jwt.init_app(app)
    app.jwt = jwt

    # initialize CSRFProtect instance
    csrf.init_app(app)
    app.csrf = csrf

    # create SMTP handler and added to the root logger
    mail_handler = SMTPHandler(
        mailhost=(
            app.config['MAIL_SERVER'],
            app.config['MAIL_PORT']
        ),
        fromaddr=app.config['MAIL_DEFAULT_SENDER'],
        toaddrs=['steveadahson@gmail.com'],
        subject='System error - log'
    )
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(formatter)
    app.logger.addHandler(mail_handler)

    with app.app_context():
        # import all the models from app/models/__init__.py
        from app.models import Admin, FeaturedProject, ProjectDone, \
        Writing, Reference, Resume, ContactMessage
        db.create_all()
        app.logger.info("DB Tables created successfully")

        from app.config import create_default_admin
        create_default_admin()
        app.logger.info("Default Admin created successfully")

        # import main blueprint
        from app.routes import bp

        # register main blueprint to app
        app.register_blueprint(bp)

    return app
