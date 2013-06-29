from django.utils import simplejson
from dajaxice.decorators import dajaxice_register


@dajaxice_register
def chat(request, text):

    f = open("log.html", "a")
    f.write("\n %s" % text)
    f.close()
    f = open("log.html", "r")
    log = f.read()
    f.close()
    return simplejson.dumps({'message':log})
