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


class ProductionCfg(Config):
    pass
