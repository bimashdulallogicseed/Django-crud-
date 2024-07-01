from typing import Any
from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=250)
    email= models.EmailField()
    password = models.CharField(max_length=120)
    
    def __str__(self):
       return self.name
   