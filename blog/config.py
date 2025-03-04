from datetime import datetime
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Config():
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.environ.get("SECRET_KEY")


class DevelopmentCfg(Config):
    DEBUG = True
    APP_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
    VIEWS_DIR = APP_DIR / "template"
    CONTROLLER_DIR = APP_DIR / "controllers"
    STATIC_DIR = APP_DIR / "static"
    IMAGES_DIR = STATIC_DIR / "images"
    #postgresql
    SQLALCHEMY_DATABASE_URI = f'postgresql://{os.environ.get("DATABASE_USERNAME")}:{os.environ.get("DATABASE_PASSWORD")}@localhost/{os.environ.get("DATABASE_NAME")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Owner data
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
    OWNER_EMAIL = os.environ.get("OWNER_EMAIL")
    OWNER_PASSWORD = os.environ.get("OWNER_PASSWORD")
    # Seed Data
    ACCOUNT_COUNT = 20
    ADMIN_PERCENTAGE = 10  # 10%
    USER_PASSWORD = '123'
    ARTICLE_COUNT = 100
    CUSTOMER_COUNT = 40
    START_DATE = datetime(2023, 2, 1)
    LIKE_COUNT = 500


class ProductionCfg(Config):
    pass
