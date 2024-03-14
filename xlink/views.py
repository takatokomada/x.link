from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from django.shortcuts import redirect
def index(request):
    template = loader.get_template('index.html')
    context_instance = {
        'csrf_token': '',
    }
    return HttpResponse(template.render(context_instance, request))
def home(request):
    template = loader.get_template('home.html')
    context = {
        'csrf_token': '',
    }
    return HttpResponse(template.render(context, request))