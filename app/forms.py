from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Domain
from app import application

# TODO add a better validator
#   check kerberos ID (or email if a alias ?)
#   check domain, verify whois ?
class AddDomainForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    domain = StringField('Domain', validators=[DataRequired()])
    submit = SubmitField('Add the domain')

    def validate_email(self, email):
        d = application.config.get('EMAIL_DOMAIN')
        if d:
            if not email.data.split('@')[-1].lower() == d.lower():
                raise ValidationError("Invalid email domain entered, should be %s" % d)


    def validate_domain(self, domain):
        domain = Domain.query.filter_by(domain=domain.data.lower().strip()).first()
        if domain is not None:
            raise ValidationError("Domain already entered")
        # TODO
