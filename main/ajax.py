from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.contrib.auth.models import User
import main
import friends
from django.utils import timezone



@dajaxice_register
def new_post(request, newtext):
    try:
        p = User.objects.get(username = request.session['username'])
    except:
        return simplejson.dumps({'message':'user problem, logout & login to fix the problem'})
    try:
        post = main.models.Post.objects.create(user = p, date = timezone.now(), text = newtext)
        post.save()
        return simplejson.dumps({'message':'you posted your status successfully!'})
    except:
        return simplejson.dumps({'message':'post saving problem, try again...'})
    

    
@dajaxice_register
def update(request):
    posts = list(main.models.Post.objects.all())
    posts = posts[-20:]
    html = ''
    now = timezone.now()
    time = ("%s" %now)
    time = time[:16]
    id = 0
    for i in reversed(posts) :
        id += 1
        html += '<p> #'+ str(id) +' <br>' + i.user.first_name + ' ' + i.user.last_name + ' updated status '  + ' : ' + "<br>" + i.text + "</P>" + time + " <hr width='33%'>"
    return simplejson.dumps({'data':html})

@dajaxice_register
def search_poeple(request, name):
    try:
        namelist = name.split()
        fname    = namelist[0]
        lname    = namelist[1]
        p = User.objects.get(first_name = fname, last_name = lname)
    except:
        return simplejson.dumps({'html':'search result did not match, try again...'})
    try:
        html = ''
        link = '  <a href="javascript:Dajaxice.main.add_friend(addfriend, {' + "'username' : " + "'" + str(p.username)+ "'" + '});"' + '>Add friend</a>'
        print link
        html += p.first_name + ' ' + p.last_name + link
        
        return simplejson.dumps({'html': html})
    except:
        return simplejson.dumps({'html':'html error'})

@dajaxice_register
def add_friend(request, username):
    try:
        fuser = User.objects.get(username = request.session['username'])
        tuser = User.objects.get(username = username)
    except:
        return simplejson.dumps({'html': "user finding error!"})
    
    try:
        print 1
        if not friends.models.Friendship.objects.are_friends(fuser, tuser):
            friendship = friends.models.Friendship(to_user = tuser, from_user = fuser)
            friendship.save()
            return simplejson.dumps({'html': "you're now friend "})
            # with %s %s" %(tuser.first_name, tuser.last_name)})
        else:
            return simplejson.dumps({'html': "Already friends!"})
    except:
        return simplejson.dumps({'html': "all error!"})