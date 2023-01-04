from django import forms
from .models import Users
from .tasks import send_email_task

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    attach = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget = forms.Textarea)

    def send_email(self, files):
        emails = [email.email for email in Users.objects.all()]
        # print("i am inside send email")
        # send_email_task.delay(
        #     self.cleaned_data['subject'],
        #     self.cleaned_data['message'],
        #     emails,
        #     files
        # )
        send_email_task(
            self.cleaned_data['subject'],
            self.cleaned_data['message'],
            emails,
            files
        )