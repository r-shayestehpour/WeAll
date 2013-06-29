from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from forms import ContactForm
from dajaxice.core import dajaxice_autodiscover 

dajaxice_autodiscover()
 
def contact_form(req):
    return render(req, "contact_form.html", {'form':ContactForm()})

def test (request):
    t = loader.get_template('chat/chat.html')
    c = Context({
        'name': 'Meraj',
    })
    return HttpResponse( t.render(c) )


