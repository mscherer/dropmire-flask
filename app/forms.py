from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

# TODO add a better validator
#   check kerberos ID (or email if a alias ?)
#   check domain, verify whois ?
class AddDomainForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    domain = StringField('Domain', validators=[DataRequired()])
    submit = SubmitField('Add the domain')
