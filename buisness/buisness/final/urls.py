from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("invoice", views.invoice, name="invoice"),
    path("generate_invoice", views.generate_invoice, name="generate_invoice"),
    path("history", views.invoice_history, name="history"),
]
