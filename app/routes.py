from flask import render_template, flash, redirect
from app import application
from app import db
from app.forms import AddDomainForm
from app.models import Domain

@application.route('/')
@application.route('/index')
def index():
    domains = Domain.query.all()
    return render_template('index.html', domains=domains)

@application.route('/add.html', methods=['GET', 'POST'])
def add():
    form = AddDomainForm()
    if form.validate_on_submit():
        domain = Domain(domain=form.domain.data.lower().strip(),
                        email=form.email.data.lower().strip())
        db.session.add(domain)
        db.session.commit()

        flash('Domain {} added'.format(
            form.domain.data))
        return redirect('/index')

    return render_template('add.html', form=form)

@application.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error=error)

