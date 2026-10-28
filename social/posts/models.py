from django.db import models
from accounts.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField()
    likes = models.ManyToManyField(User, related_name='Like_Account')
    picture = models.ImageField(upload_to='post/', default='', null=True, blank=True)

class Comment(models.Model):
    comment = models.CharField(max_length=50)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)