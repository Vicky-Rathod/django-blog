from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag()
def recent_post_lists(num=5):
    recent_post_list = Post.post_manager.all()[:num]
    return recent_post_list

@register.simple_tag()
def common_hashtags(num=10):
    common_tags = Post.hashtags.most_common()[:num]
    return common_tags