from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
# thirt perty app import
from taggit.managers import TaggableManager

User = settings.AUTH_USER_MODEL


class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(PostManager, self).get_queryset(*args, **kwargs).filter(status='Publish')
class Post(models.Model):
    CHOICES_STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft')
    )
    user = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    slug = models.SlugField(_("slug"), unique=True, blank=True, max_length=150)
    description = models.TextField(_("description"))
    hashtags = TaggableManager()
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)
    favorites = models.ManyToManyField(
                                    User, related_name='favorites',
                                    default=None, blank=True)
    status = models.CharField(_("Status"), choices=CHOICES_STATUS, default='Draft', max_length=12)
    created_at = models.DateTimeField(_("Create time"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(_("Update time"), auto_now=True, auto_now_add=False)

    objects = models.Manager()
    post_manager = PostManager()

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.all().count()
    
    def total_dislikes(self):
        return self.dislikes.all().count()
    
    def total_comment(self):
        return self.comments.all().count()
    
    class Meta:
        ordering = ('-created_at',)
    
    def get_absolute_url(self):
        return reverse('blog:single_post_view', kwargs={'slug': self.slug})
    