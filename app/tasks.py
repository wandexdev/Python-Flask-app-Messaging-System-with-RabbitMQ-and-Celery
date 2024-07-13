from celery_config import celery
from email_utils import send_email
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@celery.task
def send_email_task(email):
   # send_email(email)

    try:
        send_email(email)
        logger.info(f"Email sent to {email}")
    except Exception as e:
        logger.error(f"Error sending email to {email}: {e}")

