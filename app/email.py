import jwt
from app import application
from flask_mail import Message
from app import mail
from app.models import in_1_week
from flask import render_template

def send_email(subject, sender, recipients, text_body, html_body=None):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    if html_body:
        msg.html = html_body
    mail.send(msg)

def send_verification_email(domain, email):

    token = jwt.encode(
            {'domain': domain, 
             'expire': in_1_week().isoformat(),
             'email': email},
            application.config['SECRET_KEY'], 
            algorithm='HS256').decode('utf-8')

    recipients = sender=application.config['ADMINS']
    recipients.append(email)

    send_email('[Dropmire] New domain added',
               sender=application.config['MAIL_FROM'],
               recipients=recipients,
               text_body=render_template('email/new_domain.txt',
                                        domain=domain, email=email,
                                        token=token))
