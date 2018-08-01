from flask import render_template
from app import application
from app import db


@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')


@application.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error=error)

