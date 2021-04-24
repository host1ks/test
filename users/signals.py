from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Blog


@receiver(post_save, sender=User)
def create_blog(created, instance, **kwargs):
    if created:
        new_blog = Blog(
            author=instance,
            name=f'Blog {instance.username}'
        )
        new_blog.save()
