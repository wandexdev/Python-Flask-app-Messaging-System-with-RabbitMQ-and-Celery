from celery_config import celery
from email_utils import send_email

@celery.task
def send_email_task(email):
    send_email(email)

