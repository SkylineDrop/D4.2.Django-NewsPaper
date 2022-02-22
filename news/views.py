from django.views.generic import ListView, DetailView

from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'news.html' 
    context_object_name = 'news'
    ordering = ['created_at']

class PostDetail(DetailView):
    model = Post
    template_name = 'current_news.html' 
    context_object_name = 'current_news'