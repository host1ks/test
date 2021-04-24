from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField('Название', max_length=100)


class Post(models.Model):
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE)
    header = models.CharField('Заголовок', max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.header
