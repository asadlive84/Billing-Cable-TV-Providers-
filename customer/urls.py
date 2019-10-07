from django.urls import path
from customer import views

app_name = 'customer'

urlpatterns = [
    path('', views.customer_list, name="customer_list"),
    path('customer_details/<slug:slug>/', views.customer_details, name="customer_details"),
    path('customer_details_edit/<slug:slug>/', views.edit_customer, name="customer_details_edit"),
    path('create_customer/', views.create_customer, name="create_customer"),
    path('create_invoice/<str:customer_id>/', views.create_invoices, name="create_invoices"),
]