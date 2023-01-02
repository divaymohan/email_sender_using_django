from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from celery import shared_task

@shared_task
def add(x,y):
    return x+y
