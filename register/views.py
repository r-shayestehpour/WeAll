from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.template import Context, loader
from django.utils import timezone
import main
import random

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
    birth_date = request.POST['birth_date']
    gender     = request.POST['gender']
    
    usr            = User.objects.create_user(email, email, password)
    usr.first_name = first_name
    usr.last_name  = last_name
    p              = main.models.Person.objects.create( user = usr, gender = gender, join_date = timezone.now(), birth_date = birth_date )
    
    usr.save()
    p.save()
    
    template = loader.get_template(TEMPLATE_DIRS[0] +'/main/index.html')
    message = "You're successfully signed up!\nLogin & Enjoy!"
    return HttpResponse(template.render(Context({'message' : message, 'random':int(random.random()*24)})))
