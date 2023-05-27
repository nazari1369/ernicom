from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def Login(request):
  template = loader.get_template('users/login.html')
  return HttpResponse(template.render())