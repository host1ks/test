from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import View

from users.forms import SubscribeForm
from users.models import Subscribe, Read
from .models import Post, Blog
from .forms import PostForm


class Main(View):
    def get(self, request):
        read = []
        posts = Post.objects.all().order_by('-date_posted')
        if request.user.id:
            read = Read.objects.filter(user=request.user).values_list('post', flat=True)

        return render(request, 'main/home.html', context={'posts': posts, 'read': read})

    def post(self, request):
        read = request.POST
        for k in read.keys():
            if 'read' in k:
                new_obj = Read(
                    user=request.user,
                    post=Post.objects.get(id=k.split('_')[1]),
                    status=1
                )
                new_obj.save()
        return redirect('/')


class NewPost(View):

    def get(self, request):
        return render(request, 'main/post.html',
                      context={'form': PostForm(), 'blog': Blog.objects.get(author_id=request.user),
                               'posts': Post.objects.filter(blog__author_id=request.user)})

    def post(self, request):
        post = PostForm(request.POST)
        if post.is_valid():
            new_post = post.save()
            list_subs = Subscribe.objects.filter(blog_id=new_post.blog.id).values_list('sub_user__email', flat=True)
            send_mail('Новый пост на сайте', f'Ссылка на пост: http://localhost:8000/post/{new_post.id}',
                      'programm_test@ukr.net', list(list_subs), fail_silently=True)
        return redirect('/posts')


class PostDetail(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        read = Read.objects.filter(user=request.user, post=post)
        if not read.exists():
            new_read = Read(
                user=request.user,
                post=post,
                status=1
            )
            new_read.save()
        return render(request, 'main/post_detail.html', context={'post': post})


class BlogDetail(View):
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        posts = Post.objects.filter(blog__author_id=blog.author)
        list_subs = Subscribe.objects.filter(Q(sub_user=request.user) & Q(blog_id=blog_id))
        if list_subs.exists():
            list_subs = True
        return render(request, 'main/blog_detail.html', context={'blog': blog, 'posts': posts, 'sub': list_subs})

    def post(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        list_subs = Subscribe.objects.filter(Q(sub_user=request.user) & Q(blog_id=blog_id))
        form = SubscribeForm({'sub_user': request.user.id, 'blog': blog.id})
        if list_subs.exists():
            list_subs.delete()
        else:
            if form.is_valid():
                form.save()
        return redirect(f'/blog/{blog_id}')


class News(View):
    def get(self, request):
        list_subs = Subscribe.objects.filter(sub_user=request.user).values('blog')
        return render(request, 'main/news.html',
                      context={'posts': Post.objects.filter(blog__in=list_subs).order_by('-date_posted')})
