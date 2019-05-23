from django.db import models
from django.contrib.auth.models import User
# Create your models here.
 
class Person(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)

    def __unicode__(self):
        return self.user


