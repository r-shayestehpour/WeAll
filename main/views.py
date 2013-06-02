__author__ = 'arash'

from django.template import Context, loader
from django.http import HttpResponse
import main

def index (request) :
    template = loader.get_template('/home/arash/apProjects/sn/WeAll/main/templates/index.html')
    return HttpResponse(template.render(Context({})))

def home (request) :
    template = loader.get_template('/home/arash/apProjects/sn/WeAll/main/templates/home.html')
    if request.session.get('username') :
        p = main.models.Person.objects.get(username = request.session['username'])
        return HttpResponse(template.render(Context({'person':p})))
    else :
        return HttpResponse("Please login first ... <br/>"
                            "to login clock <a href='/'> here </a>")