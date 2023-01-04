from django.urls import path
from tableview.views import TableView

urlpatterns = [
    path('', TableView.as_view(), name='tableview')
]
