from django.contrib.auth.models import User

from news.models import Author, Category, Comment, Post, PostCategory

user_1, user_2 = User.objects.filter()
author_1, author_2 = Author.objects.filter()
cat_it, cat_sci, cat_gms, cat_spt = Category.objects.filter()
post_neuroimp, post_vrh, post_django = Post.objects.filter()
comm_1, comm_2, comm_3, comm_4 = Comment.objects.filter()

# 1. 
user_1 = User.objects.create_user(username='Dan Abnett',  password='123')
user_2 = User.objects.create_user(username='Graham McNeill', password='123')

# 2.
author_1 = Author.objects.create(user=user_1)
author_2 = Author.objects.create(user=user_2)

# 3.
cat_it = Category.objects.create(name='it')
cat_sci = Category.objects.create(name='science')
cat_gms = Category.objects.create(name='games')
cat_spt = Category.objects.create(name='sport')

# 4.
post_neuroimp = Post.objects.create(
    author=author_1,
    post_type=Post.article,
    header='Интервью с первым бегуном, использующим нейроимпланты',
    content='https://youtube.com/?v=lorem-ipsum',
)

post_vrh = Post.objects.create(
    author=author_2,
    post_type=Post.article,
    header='Facebook продемонстрировали новый VR-шлем',
    content='https://youtube.com/?v=lorem-ipsum',
)

post_django = Post.objects.create(
    author=author_1,
    post_type=Post.news,
    header='Британские учёные научились использовать Django',
    content='plain text',
)

 # 5.
PostCategory.objects.create(post=post_neuroimp, category=cat_sci)
PostCategory.objects.create(post=post_neuroimp, category=cat_spt)
PostCategory.objects.create(post=post_vrh, category=cat_gms)
PostCategory.objects.create(post=post_vrh, category=cat_it)
PostCategory.objects.create(post=post_django, category=cat_it)

# 6.
comm_1 = Comment.objects.create(
    post=post_neuroimp,
    user=user_2,
    content='съешь мягких булочек',
)

comm_2 = Comment.objects.create(
    post=post_neuroimp,
    user=user_2,
    content='съешь ещё мягких булочек',
)

comm_3 = Comment.objects.create(
    post=post_vrh,
    user=user_1,
    content='регаться на fb ради шлемов не стоит того',
)

comm_4 = Comment.objects.create(
    post=post_django,
    user=user_2,
    content='молодцы',
)

# 7.
post_neuroimp.like()
post_vrh.dislike()
comm_1.like()

# 8.
author_1.update_rating()
author_2.update_rating()

# 9.
'{0.user.username} {0.rating}'.format(Author.objects.order_by('-rating')[0])

# 10.
best_post = Post.objects.filter(post_type=Post.article).order_by('-rating')[0]
post_date = best_post.created_at.strftime("%A %d. %B %Y")
post_author_name = best_post.author.user.username
post_current_rating = best_post.rating
post_header = best_post.header
post_prev = best_post.preview()

res = f'{post_date} {post_author_name} {post_current_rating} {post_header} {post_prev}'

# 11.
comments = Comment.objects.filter(post=best_post)
res = [f'{comment.created_at.strftime("%A %d. %B %Y")} {comment.user} {comment.rating} {comment.content}' for comment in comments]
res[0]
res[1]
