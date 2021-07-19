from django.conf import settings
from django.db import models
from blog.models import Post

LIKE_CHOICE = (
    ('like', 'Like'),
    ('unlike', 'Unlike'  )
)
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.CharField(choices=LIKE_CHOICE, max_length=10)

DISLIKE_CHOICE = (
    ('dislike', 'Dislike'),
    ('undisklike', 'Undisklike'  )
)
class Dislike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    disklikes = models.CharField(choices=DISLIKE_CHOICE, max_length=15)