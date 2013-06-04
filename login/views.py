# Create your views here.

from django.http import HttpResponseRedirect , HttpResponse
from django.template import Context, loader
from django.utils import timezone

import main
from main.settings import TEMPLATE_DIRS


def login (request ) :
    try:
        usr = request.POST['username']
        pwd = request.POST['password']
    except :
        return HttpResponseRedirect('/')

    if main.models.Person.objects.filter (username = usr , password = pwd) :
        request.session['username'] = usr
        ####################################
        request.session['expiry'] = 2
        ####################################
        p = main.models.Person.objects.get(username = usr)
        p.last_login = timezone.now()
        p.save()
        request.session.set_expiry (0)
        return HttpResponseRedirect('/home')
    else :
        template = loader.get_template(TEMPLATE_DIRS[0] +'/system_message.html')
        message = 'your username or password is wrong ! please login again'
        messageType = 'Login error !'
        return HttpResponse(template.render(Context({'message' : message , 'message_type' : messageType})))
def logout (request) :
    try :
        del request.session['username']
        del request.session['expiry']
    except KeyError :
        pass
    return HttpResponseRedirect('/')
