__author__ = 'arash'

from django.http import HttpResponseRedirect , HttpResponse
from django.template import Context, loader
from django.utils import timezone
import main

from main.settings import TEMPLATE_DIRS

def index (request) :
    template = loader.get_template(TEMPLATE_DIRS[0] +'/register/index.html')
    countries = main.models.Country.objects.all()
    context = Context ({'country_list' : countries})
    return HttpResponse(template.render(context))