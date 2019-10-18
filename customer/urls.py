from django.urls import path
from customer import views
from customer import serializers_view
app_name = 'customer'

urlpatterns = [
    path('', views.home_page, name="home"),
    path('customer_list/', views.customer_list, name="customer_list"),
    path('customer_details/<str:slug>/', views.customer_details, name="customer_details"),
    path('customer_details_edit/<str:slug>/', views.edit_customer, name="customer_details_edit"),
    path('create_customer/', views.create_customer, name="create_customer"),
    path('create_invoice/<str:customer_id>/', views.create_invoices, name="create_invoices"),
    path('create_package/', views.create_package, name="create_package"),
    path('create_union/', views.create_union, name="create_union"),
    path('create_word/', views.create_word, name="create_word"),
    path('create_bill/', views.create_bill, name="create_bill"),



    path('api/', serializers_view.CustomerListAPI.as_view(), name="customer_list_api")
]