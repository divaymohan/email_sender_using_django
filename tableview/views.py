from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from django.core.mail import EmailMessage

from django.conf import settings


class TableView(View):
    # form_class = EmailForm
    template_name = 'tableview/table.html'
    data = {
        "name": "this is my data",
        "wbs_data": [{
            "wbs": "S22-2001",
            "description": "Project kick off",
            "milestone_due_date": "12/1/2022",
            "Cap_or_Exp": "Capital",
            "sow_mso_amount": 50000,
            "haea_invoice":1234,
            "haea_invoice_date":"12/1/2022",
            "status":"Invoiced"

        },
        {
            "wbs": "S22-2001",
            "description": "Project kick off",
            "milestone_due_date": "12/1/2022",
            "Cap_or_Exp": "Capital",
            "sow_mso_amount": 50000,
            "haea_invoice":1234,
            "haea_invoice_date":"12/1/2022",
            "status":"Invoiced"

        },
        {
            "wbs": "S22-2001",
            "description": "Project kick off",
            "milestone_due_date": "12/1/2022",
            "Cap_or_Exp": "Capital",
            "sow_mso_amount": 50000,
            "haea_invoice":1234,
            "haea_invoice_date":"12/1/2022",
            "status":"Invoiced"

        },
        {
            "wbs": "S22-2001",
            "description": "Project kick off",
            "milestone_due_date": "12/1/2022",
            "Cap_or_Exp": "Capital",
            "sow_mso_amount": 50000,
            "haea_invoice":1234,
            "haea_invoice_date":"12/1/2022",
            "status":"Invoiced"

        },]
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'data': self.data})

   