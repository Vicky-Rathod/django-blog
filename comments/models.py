from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from blog.models import Post
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                            verbose_name=_("user"), 
                            on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f'Comment by {self.user.username}'
    
    def get_absolute_url(self):
        return reverse('blog:single_post_view', kwargs={'slug': self.slug})
