from django.template.loader import render_to_string
from django.core.mail import EmailMessage


from celery import shared_task
from .email import send_email

# @shared_task(name="send_email_task")
def send_email_task(subject, message, emails, files):
    # print("i am inside task")
    return send_email(subject=subject,message=message,emails=emails,files=files)



