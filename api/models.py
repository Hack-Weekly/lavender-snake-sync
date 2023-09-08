from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):   
    pass
    def __str__(self):
        return self.username

class Event(models.Model):
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=50, null=False, blank=False) #event name
    event_note = models.CharField(max_length=150, blank=True, null=True) #event name
    is_public = models.BooleanField(null=False,default=True) #True: Event is public, False: Event is private
    event_start = models.DateTimeField() 
    event_end = models.DateTimeField() 
    members= models.ManyToManyField("Availability",related_name='members',blank=True) #members of event

    def __str__(self):
        return self.name

class Availability(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    start = models.DateTimeField() #start time of event
    end = models.DateTimeField() #end time of event
    def __str__(self):
        return self.user.username + " " + self.event.name
    
