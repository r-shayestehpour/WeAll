__author__ = 'arash'

from django.template import Context, loader
from django.http import HttpResponse

def index (request) :
    template = loader.get_template('/home/arash/apProjects/sn/WeAll/main/templates/index.html')
    return HttpResponse(template.render(Context({})))

def home (request) :
    template = loader.get_template('/home/arash/apProjects/sn/WeAll/main/templates/home.html')
    return HttpResponse(template.render(Context({})))
