from django.db import models
from django.contrib.auth.models import User

class Country (models.Model) :
    country_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.country_name

class Person (models.Model) :
    user       = models.OneToOneField(User)
    phone_num  = models.CharField(max_length=20, null = True)
    country    = models.ForeignKey(Country, null = True)
    birth_date = models.DateTimeField("birth date")
    GENDERS    = (
                  ('M','Male'),
                  ('F','Female'),
                  )
    gender     = models.CharField(max_length = 1, choices = GENDERS)
    join_date  = models.DateTimeField("join date", null = True)
    last_login = models.DateTimeField("last login", null = True)
    
    def __unicode__(self):
        return self.user.first_name + " " + self.user.last_name
    
class Post (models.Model):
    person = models.ForeignKey(Person)
    date   = models.DateTimeField("post date")
    

#TODO:inai k az inja mizanam ro ezafe kn!
#gender:male/female#
#hometown
#highschool
#college/university
#ye feild bara description: matn bayad bezanan < 1000ch
