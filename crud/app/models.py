from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UserModel(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.CharField(max_length=128)  # Stores hashed password
    image=models.ImageField(upload_to='static/images/',default='')
    
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name
