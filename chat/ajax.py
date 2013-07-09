from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.contrib.auth.models import User
from django.utils import timezone


@dajaxice_register
def chat(request, text):
    try:
        p = User.objects.get(username = request.session['username'])
        name = p.last_name
    except:
        name = "unknown"
    now = timezone.now()
    time = ("%s" %now)
    time = time[:16]
    f    = open("log.html", "a")
    f.write("<br> <b>%s </b>: %s <br> <small color='Silver'> (%s)</small>" %(name, text, time))#TODO inja chato khoshgel mknm
    f.close()
    f    = open("log.html", "r")
    log  = f.read()
    f.close()
    return simplejson.dumps({'message':log})

@dajaxice_register
def update_chat(request):
    f    = open("log.html", "r")
    log  = f.read()
    f.close()
    return simplejson.dumps({'message':log})
