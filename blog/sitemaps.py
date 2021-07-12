from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self, *args, **kwargs):
        return Post.objects.filter(status='Publish')

    def lastmod(self, obj):
        return obj.updated_at