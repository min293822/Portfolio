from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  email = models.EmailField(max_length=199, unique = True)
  birth_date = models.DateField()
  sex = models.CharField(max_length=20, choices =[
    ('F','Female'),
    ('M','Male'),
    ('O','Other')
    ])
  password = models.CharField(max_length=200)
  

