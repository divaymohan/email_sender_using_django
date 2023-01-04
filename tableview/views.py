from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.core.mail import EmailMessage

from django.conf import settings


class TableView(View):
    # form_class = EmailForm
    template_name = 'tableview/table.html'
    data = {"name": "this is my data"}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'data': self.data})

   