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

def sign_up (request):
    first_name = request.POST['name']
    last_name  = request.POST['family']
    email      = request.POST['email']
    password   = request.POST['password']
    con_pass   = request.POST['con_pass']
    birth_date = request.POST['birth_date']
    gender     = request.POST['gender']
    
    user            = User.objects.create_user(email, email, password)
    user.first_name = first_name
    user.last_name  = last_name
    user.birth_date = birth_date
