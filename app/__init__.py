from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config.from_object(Config)

db = SQLAlchemy(application)

from app import routes

if __name__ == "__main__":
    application.run()

