from django.forms import ModelForm
from main.models import Blog, Post


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ["author", "name"]


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["header", "text", "blog"]
