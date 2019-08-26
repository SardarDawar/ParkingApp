from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save



# Create your models here.
class userProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    can_upload = models.BooleanField(default=False)
    unchecked = models.BooleanField(default=True)
    profile_pic = models.ImageField(default='blank-profile-picture-973460_640.png',blank=True)
   
    @receiver(post_save, sender=User)
    def create_person(sender, instance, created, **kwargs):
        if created:
            userProfile.objects.create(user = instance)
        try:
            instance.userprofile.save()
        except:
            userProfile.objects.create(user = instance)
    def __str__(self):
        return str(self.user)

class Employee(models.Model):
    person = models.ForeignKey(User, default = 1, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=32,null=True,blank=True)
    number = models.CharField(max_length=15,null=True,blank=True)   
    profile_pic = models.ImageField(default='blank-profile-picture-973460_640.png',blank=True)
    def __str__(self):
        return str(self.person.first_name)+" "+str(self.person.last_name)
