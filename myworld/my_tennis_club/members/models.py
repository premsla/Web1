from django.db import models

#Create your models here.
class Account_Details(models.Model):
     First_Name = models.CharField(max_length = 30)
     Last_Name = models.CharField(max_length = 30)
     Emails = models.CharField(max_length = 30)
     Contact_no = models.IntegerField(12)
     Address = models.TextField()
    # profiles/models.py

#from django.db import models
#from django.contrib.auth.models import User

#class UserProfile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #bio = models.TextField(blank=True)
    # Add any other fields you want for the profile

    #def __str__(self):
        #return self.user.username
 
