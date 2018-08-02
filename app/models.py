# no auto, need 3.6
from enum import Enum
from app import db
import datetime

# hardcoded to be 6 months
def in_6_months():
    return datetime.date.today()  + datetime.timedelta(weeks=26)

class PhaseEnum(Enum):
    # when we match a subdomain
    sub_domain = 1
    # when subdomain get no answer
    root_domain = 2
    # when no one answer
    manager = 3

class Domain(db.Model):
    domain = db.Column(db.String(64), index=True, unique=True, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=False)
    next_phase = db.Column(db.Enum(PhaseEnum), default=PhaseEnum.sub_domain)
    next_mail_date = db.Column(db.Date(), default=in_6_months())
    first_attempt = db.Column(db.Boolean(), default=True)
