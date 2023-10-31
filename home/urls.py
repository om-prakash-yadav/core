from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import InvoiceListView, createInvoice, view_PDF, generate_PDF

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('tables/', views.tables, name='tables'),
  path('invoice-list', InvoiceListView.as_view(), name="invoice-list"),
  path('create/', createInvoice, name="invoice-create"),
  path('remove-invoice/', views.remove_invoice, name='remove-invoice'),
  path('invoice-detail/<id>', view_PDF, name='invoice-detail'),
  path('invoice-download/<id>', generate_PDF, name='invoice-download'),
  path('generate_appointment_letter/', views.generate_appointment_letter, name='generate_appointment_letter'),
  path('generate_introductory_letter/', views.generate_introductory_letter, name='generate_introductory_letter'),
  path('generate-offer-letter/', views.generate_offer_letter, name='generate_offer_letter'),
  path('generate_offer_letter_content/', views.generate_offer_letter_content, name='generate_offer_letter_content'),
]
