from main.settings import *

__author__ = 'arash'

from django.template import Context, loader
from django.http import HttpResponse
import main

def index (request) :
    template = loader.get_template(TEMPLATE_DIRS[0]+'/index.html')
    return HttpResponse(template.render(Context({'temp_dir':TEMPLATE_DIRS[0] , 'MEDIA_DIR' : MEDIA_URL})))

def home (request) :
    template = loader.get_template(TEMPLATE_DIRS[0]+'/home.html')
    if request.session.get('username') :
        p = main.models.Person.objects.get(username = request.session['username'])
        return HttpResponse(template.render(Context({'person':p})))
    else :
        template = loader.get_template(TEMPLATE_DIRS[0]+'/system_message.html')
        message = 'you are not logged in ! please first login ...'
        return HttpResponse(template.render(Context({'message' : message})))