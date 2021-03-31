from django.urls import path

from . import views
from . import forms

app_name = 'polls'


urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("success.html", views.success, name="success"),
    path("failure.html", views.failure, name="failure"),
    path("", views.login_request, name="login"),
    path("polls/login.html", views.login_request, name="login")



]