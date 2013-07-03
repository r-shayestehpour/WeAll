from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.contrib.auth.models import User
from main import models
from django.utils import timezone



@dajaxice_register
def new_post(request, newtext):
    try:
        p = User.objects.get(username = request.session['username'])
    except:
        return simplejson.dumps({'message':'user problem, logout & login to fix the problem'})
    try:
        post = models.Post.objects.create(user = p, date = timezone.now(), text = newtext)
        post.save()
        return simplejson.dumps({'message':'you posted your status successfully!'})
    except:
        return simplejson.dumps({'message':'post saving problem, try again...'})
    

    
@dajaxice_register
def update(request):
    posts = models.Post.objects.all()[:20]
    html = ''
    now = timezone.now()
    time = ("%s" %now)
    time = time[:16]
    for i in posts :
        html += '<p>' + i.user.first_name + ' ' + i.user.last_name + ' updated status '  + ' : ' + "<br>" + i.text + "</P>" + time + " <hr width='33%'>"
    return simplejson.dumps({'data':html})