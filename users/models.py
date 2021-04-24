from django.contrib.auth.models import User
from django.db import models
from main.models import Blog, Post


class Subscribe(models.Model):
    sub_user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class Read(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
