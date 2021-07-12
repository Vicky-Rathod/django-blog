from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag()
def recent_post_lists(num=5):
    return Post.post_manager.all()[:num]