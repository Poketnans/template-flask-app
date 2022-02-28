import os
from datetime import timedelta


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    JWT_SECRET_KEY = os.getenv('SECRET', 'AsGeNgIoJeRTUu1VQDbpbg')

    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')


config_selector = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
