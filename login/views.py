# Create your views here.

from django.http import HttpResponseRedirect , HttpResponse
from django.template import Context, loader
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

import main
import random
from main.settings import TEMPLATE_DIRS



def login (request ) :
    try:
        usr = request.POST['email']
        pwd = request.POST['password']
    except :
        return HttpResponseRedirect('/')
    usr = authenticate(username = usr, password = pwd)
    if usr is not None :
        request.session['username'] = usr
        ####################################
        request.session['expiry'] = 2
        ####################################
        #user.person.last_login = timezone.now()
        #user.person.save()
        p = main.models.Person.objects.get(user = usr)
        p.last_login = timezone.now()
        p.save()
        request.session.set_expiry (0)
        return HttpResponseRedirect('/home')
    else :
        template = loader.get_template(TEMPLATE_DIRS[0] +'/main/index.html')
        message = 'Wrong email or password!'
        return HttpResponse(template.render(Context({'message' : message, 'random':int(random.random()*26)})))
def logout (request) :
    try :
        del request.session['username']
        del request.session['expiry']
    except KeyError :
        pass
    return HttpResponseRedirect('/')

