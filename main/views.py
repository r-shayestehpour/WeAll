from main.settings import TEMPLATE_DIRS, ROOT
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
import main
import random

def index (request) :
    #############################################
    if request.session.get('expiry') == -1 :
        return HttpResponseRedirect('/login/close/')
    #############################################
    elif request.session.get('username') :
        return HttpResponseRedirect('/home')
    #############################################
    else:
        template = loader.get_template(TEMPLATE_DIRS[0]+'/main/index.html')
        return HttpResponse(template.render(Context({'random':int(random.random()*26)})))

def home (request) :
    template = loader.get_template(TEMPLATE_DIRS[0]+'/main/home.html')
    if request.session.get('username') :
        p = User.objects.get(username = request.session['username'])
        now = timezone.now()
        time = str(now)
        time = time[11:13]
        time = int(time)
        if time > 6 and time < 15 :
			time_css = "day"
        else:
			time_css = "night"
        return HttpResponse(template.render(Context({'person':p, 'time': time_css})))
    else :
        template = loader.get_template(TEMPLATE_DIRS[0]+'/system_message.html')
        message = 'you are not logged in ! please first login ...'
        messageType = 'Login error !'
        return HttpResponse(template.render(Context({'message' : message , 'message_type' : messageType})))
