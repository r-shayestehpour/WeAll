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
        now = timezone.now()
        time = str(now)
        time = time[11:13]
        time = int(time)
        print "salam"
#        if time > 6 and time < 15 :
        if True:
            print "sallma"
            f = open(ROOT+"/main/static/main/css/team.css","r")
            af = f.read()
            f.close()
            af = af.replace("background:#a7e4f3 url(../img/day.jpg) no-repeat center top;",
                "background:#022e3f url(../img/night.jpg) no-repeat center top;")
            f = open(ROOT+"/main/static/main/css/team.css","w")
            f.write(af)
            f.close()
        else:
            f = open(ROOT+"/main/static/main/css/team.css","r")
            af = f.read()
            f.close()
            af = af.replace("background:#022e3f url(../img/night.jpg) no-repeat center top;",
                "background:#a7e4f3 url(../img/day.jpg) no-repeat center top;")
            f = open(ROOT+"/main/static/main/css/team.css","w")
            f.write(af)
            f.close()
        return HttpResponseRedirect('/home')
    #############################################
    else:
        template = loader.get_template(TEMPLATE_DIRS[0]+'/main/index.html')
        return HttpResponse(template.render(Context({'random':int(random.random()*26)})))

def home (request) :
    template = loader.get_template(TEMPLATE_DIRS[0]+'/main/home.html')
    if request.session.get('username') :
        p = User.objects.get(username = request.session['username'])
        return HttpResponse(template.render(Context({'person':p})))
    else :
        template = loader.get_template(TEMPLATE_DIRS[0]+'/system_message.html')
        message = 'you are not logged in ! please first login ...'
        messageType = 'Login error !'
        return HttpResponse(template.render(Context({'message' : message , 'message_type' : messageType})))
