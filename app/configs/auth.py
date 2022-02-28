import os

from flask import Flask
from flask_jwt_extended import JWTManager


def init_app(app: Flask) -> None:
    ''' Instancia o objeto JWT. '''
    JWTManager(app)
