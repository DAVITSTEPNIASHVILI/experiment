from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# class User(models.Model):
#     username = models.CharField()
#     age = models.IntegerField()
#     email = models.EmailField()
#     password = models.CharField()
#     is_current_user = models.BooleanField(default=False)
#     profile_picture = models.ImageField(upload_to='profile/', default='')

#     def __str__(self):
#         return self.username

class User(AbstractUser):
    age = models.IntegerField()
    profile_picture = models.ImageField(upload_to='profile/', default='', null=True, blank=True)