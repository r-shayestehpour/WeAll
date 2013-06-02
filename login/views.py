# Create your views here.

from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
import main

def index (request ) :
    usr = request.GET['username']
    pwd = request.GET['password']

    if main.models.Person.objects.filter (username = usr , password = pwd) :
        request.session['username'] = usr
        return HttpResponseRedirect('/home')
    else :
        return HttpResponse ("Wrong username or password ... <br/>"
                             "<a href='/' > login again </a>")