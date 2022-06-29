from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from .models import Post
from .filters import PostFilter

class PostList(ListView):
    model = Post
    template_name = 'news.html' 
    context_object_name = 'news'
    ordering = ['created_at']
    paginate_by = 10

class PostDetail(DetailView):
    model = Post
    template_name = 'current_news.html' 
    context_object_name = 'current_news'

class Postlist(ListView):
    model = Post
    template_name = 'news_search.html' 
    context_object_name = 'news'
    ordering = ['created_at']
    paginate_by = 1

    def get_context_data(self, **kwargs): # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст
        return context