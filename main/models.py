__author__ = 'arash'

from django.db import models

def autoCount (self) :
    no = person.objects.count()
    return no+1

class person (models.Model) :
    pid = models.BigIntegerField('person_id' , default = autoCount)
    name = models.CharField ('person_name' , max_length=20)
    family = models.CharField ('person_family' , max_length=20)



# Create your models here.
