from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash

from formspree import settings
from formspree.stuff import celery
from formspree.utils import send_email


def hash_pwd(password):
    return generate_password_hash(password)


def check_password(hashed, password):
    return check_password_hash(hashed, password)


@celery.task()
def send_downgrade_email(customer_email):
    send_email(
        to=customer_email,
        subject='Successfully downgraded from {} {}'.format(settings.SERVICE_NAME,
                                                            settings.UPGRADED_PLAN_NAME),
        text=render_template('email/downgraded.txt'),
        html=render_template('email/downgraded.html'),
        sender=settings.DEFAULT_SENDER
    )
