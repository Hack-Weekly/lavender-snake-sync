from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):   
    email = models.EmailField("email address", max_length=100, unique=True)
    user_name= models.CharField("username", max_length=50, unique=True)

    USERNAME_FIELD="username"
    def __str__(self):
        return self.email

class Event(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50) #event name
    event_note = models.CharField(max_length=150, blank=True, null=True) #event name
    is_public = models.BooleanField(null=False,default=True) #True: Event is public, False: Event is private
    event_start = models.DateTimeField() #start time of event
    event_end = models.DateTimeField() #end time of event
    anonymous = models.BooleanField(null=False,default=True)
    
