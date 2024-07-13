from celery import Celery

celery = Celery('tasks', broker='pyamqp://guest@localhost//')

celery.conf.update(
    result_backend='rpc://',
)

