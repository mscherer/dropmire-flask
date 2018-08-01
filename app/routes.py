from flask import render_template, flash, redirect
from app import application
from app import db
from app.forms import AddDomainForm

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')

@application.route('/add.html', methods=['GET', 'POST'])
def add():
    form = AddDomainForm()
    if form.validate_on_submit():
        flash('Domain {} added'.format(
            form.domain.data))
        return redirect('/index')

    return render_template('add.html', form=form)

@application.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error=error)

