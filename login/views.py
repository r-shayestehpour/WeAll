# Create your views here.

from django.http import HttpResponseRedirect , HttpResponse
from django.template import Context, loader
from django.utils import timezone

import main
from main.settings import TEMPLATE_DIRS


def index (request ) :
    usr = request.GET['username']
    pwd = request.GET['password']

    if main.models.Person.objects.filter (username = usr , password = pwd) :
        request.session['username'] = usr
        p = main.models.Person.objects.get(username = usr)
        p.last_login = timezone.now()
        p.save()
        return HttpResponseRedirect('/home')
    else :
        template = loader.get_template(TEMPLATE_DIRS[0] +'/system_message.html')
        message = 'you username or password is wrong ! please login again'
        messageType = 'Login error !'
        return HttpResponse(template.render(Context({'message' : message , 'message_type' : messageType})))