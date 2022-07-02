import imp
from django_filters import FilterSet
from .models import Post

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'header': ['icontains'], # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то, что запросил пользователь
            'created_at': ['gt'], # количество товаров должно быть больше или равно тому, что указал пользователь
            'author': ['in'],
            #'everything': ['icontains'],
        }