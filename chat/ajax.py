from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.contrib.auth.models import User


@dajaxice_register
def chat(request, text):
    try:
        p = User.objects.get(username = request.session['username'])
        name = p.last_name
    except:
        name = "unknown"
    f = open("log.html", "a")
    f.write("<br> %s : %s" %(name, text))
    f.close()
    f = open("log.html", "r")
    log = f.read()
    f.close()
    return simplejson.dumps({'message':log})
