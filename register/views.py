__author__ = 'arash'

from django.http import HttpResponseRedirect , HttpResponse
from django.template import Context, loader
from django.utils import timezone
import main
import random

from main.settings import TEMPLATE_DIRS

def index (request) :
    template = loader.get_template(TEMPLATE_DIRS[0] +'/register/index.html')
    countries = main.models.Country.objects.all()
    
    return HttpResponse(template.render(Context({'country_list' : countries , 'random' : int(random.random()*2)})))
