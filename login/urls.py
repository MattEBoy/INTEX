from django.urls import path, include
from .views import loginPageView, signupPageView, enterPageView

urlpatterns = [
    path("", loginPageView, name="login"),
    path("signup", signupPageView, name="signup"),
    path("enter/", enterPageView, name="enter"),
]