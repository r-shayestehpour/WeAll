# Create your views here.

from django.http import HttpResponseRedirect , HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse



def index (request ) :
    usr = request.GET['username']
    pwd = request.GET['password']
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
     # user hits the Back button.
    # return render(request, '/home/arash/apProjects/sn/WeAll/login/templates/index.html', {
    #     'usr': usr ,'pwd' : pwd ,'error_message': "hooooooooooooy",
    #     })
    return HttpResponseRedirect('/home')