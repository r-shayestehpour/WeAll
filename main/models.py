__author__ = 'arash'

from django.db import models

class Country (models.Model) :
    country_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.country_name

class Person (models.Model) :
    name       = models.CharField (max_length=20)
    family     = models.CharField (max_length=20)
    st_num     = models.CharField (max_length=8)
    iust_mail  = models.EmailField ()
    other_mail = models.EmailField()
    phone_num  = models.CharField(max_length=20)
    language   = models.CharField(max_length=200)
    country    = models.ForeignKey(Country)
    birth_date = models.DateTimeField("birth date")
    join_date  = models.DateTimeField("join date")
    last_login = models.DateTimeField("last login")
    username   = models.CharField(max_length=20)
    password   = models.CharField(max_length=64)


# Create your models here.