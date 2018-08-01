import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE') or 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
