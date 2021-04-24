from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Post
from users.models import Subscribe


@receiver(post_save, sender=Post)
def create_blog(created, instance, **kwargs):
    if created:
        list_subs = Subscribe.objects.filter(blog_id=instance.blog.id).values_list('sub_user__email', flat=True)
        send_mail('Новый пост на сайте', f'Ссылка на пост: http://localhost:8000/post/{instance.id}',
                  'programm_test@ukr.net', list(list_subs), fail_silently=False)
