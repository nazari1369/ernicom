from django.urls import path
from . import views

urlpatterns = [
    path("", views.Login,name='Login'),
    path('social/signup/', views.signup_redirect, name='signup_redirect'),
]