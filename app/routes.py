from flask import render_template
from app import application
from app import db
from app.forms import AddDomainForm

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')

@application.route('/add.html')
def add():
   form = AddDomainForm()
   return render_template('add.html', form=form)

@application.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error=error)

