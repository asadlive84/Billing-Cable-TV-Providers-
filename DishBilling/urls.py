"""DishBilling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views, login
from user.views import user_list, user_details
from user.forms import UserLoginForm
from user.views import sign_up_form

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('customer.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('regi/', sign_up_form, name="sign_up"),
                  path('user_list/', user_list, name="user_list"),
                  path('user_details/<int:pk>/', user_details, name="user_details"),

                  path('accounts/', views.LoginView.as_view(template_name="registration/login.html",
                                                            authentication_form=UserLoginForm), name="login", ),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
