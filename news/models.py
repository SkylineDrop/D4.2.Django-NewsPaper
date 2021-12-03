from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

class RatingMixin:

    def like(self):
        self.rating = F('rating') + 1
        self.save()
        self.refresh_from_db()

    def dislike(self):
        self.rating = F('rating') - 1
        self.save()
        self.refresh_from_db()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = Post.objects.filter(author = self).aggregate(models.Sum('rating'))
        total = post_rating['rating__sum'] * 3

        comment_rating = Comment.objects.filter(user = self.user).aggregate(models.Sum('rating'))
        total += comment_rating['rating__sum']

        temp = Comment.objects.filter(post__in=Post.objects.filter(author=self)).aggregate(models.Sum('rating'))

        total += temp['rating__sum']
        self.rating = total
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Post(models.Model, RatingMixin):
    article = 'AR'
    news = 'NW' 
    POST_TYPES = [(article, 'Article'), (news, 'News')]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2 ,choices=POST_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    header = models.CharField(max_length=511)
    content = models.TextField()
    rating = models.IntegerField(default=0)

    def preview(self):
        return self.content[:124] + "..."

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model, RatingMixin):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
