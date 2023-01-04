from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def send_email(subject, message, emails, files):
    context = {
        'message': message
    }
    # print("i am inside send email")
    email_body = render_to_string('email_message.txt', context)
    print(email_body, emails, subject, settings.EMAIL_HOST_USER)
    email = EmailMessage(subject,email_body,settings.EMAIL_HOST_USER,emails)
    # mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, emails)
    for f in files:
        email.attach(f.name, f.read(), f.content_type)

    return email.send()
