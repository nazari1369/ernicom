from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def Login(request):
  template = loader.get_template('users/login.html')
  return HttpResponse(template.render())

def signup_redirect(request):
  messages.error(request, "Something wrong here, it may be that you already have account!")
  return redirect("homepage")