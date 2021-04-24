from django.urls import path
from .views import NewPost, Main, PostDetail, BlogDetail, News

app_name = 'main'
urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('posts/', NewPost.as_view(), name='posts'),
    path('post/<int:post_id>', PostDetail.as_view(), name='post'),
    path('blog/<int:blog_id>', BlogDetail.as_view(), name='blog'),
    path('news/', News.as_view(), name='news'),
]
