from flask import render_template, flash, redirect, request
from app import application
from app import db
from app.forms import AddDomainForm
from app.models import Domain
from flask import abort
from app.email import send_verification_email
import hashlib

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
        send_verification_email(domain.domain, domain.email)

        db.session.add(domain)
        db.session.commit()

        flash('Domain {} added'.format(
            form.domain.data))

        return redirect('/index')

    return render_template('add.html', form=form)

@application.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error=error)

# yes, I do like to troll people
@application.route('/cron.php', methods=['POST'])
def cron():
    data = request.form
    h = hashlib.sha256()
    h.update(application.config['SECRET_KEY'].encode())
    h.update(b'cron')
    if not "key" in data:
        abort(403)
    if data['key'] != h.hexdigest():
        abort(403)
    return "Ok !!"
    # DO cron stuff

@application.route('/verif.php?key', methods=['GET'])
def verify_domain():
    pass    

# add a link to reset the countdown
# /reset/domain/secretkey
#  secretkey being sha256
#    domain + date of next renewal + secret key
#    so if the renewal is changed, key no longer valid
#    need to decide the daate before sending the mail (to avoid corner case at midnight)
