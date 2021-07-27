from django.urls import path
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from .views import (
    HomeView,
    CreatePostView,
    SinglePostView,
    SingePostDeleteView,
    PostUpdateView,
    PostLikeView,
    PostDisLikeView,
    SingleHashTagPostList,
)

sitemaps = {
    "posts": PostSitemap,
}

app_name = 'blog'
urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('single-post/<slug>/', SinglePostView.as_view(), name='single_post_view'),
    path('delete/<slug>/', SingePostDeleteView.as_view(), name='single_post_delete_view'),
    path('add-post/', CreatePostView.as_view(), name='add_post_view'),
    path('update/<slug>/', PostUpdateView.as_view(), name='post_update_view'),
    path('like/<slug>/', PostLikeView.as_view(), name='post_like'),
    path('dislike/<slug>/', PostDisLikeView.as_view(), name='post_dislike'),
    path('ht/<slug>/', SingleHashTagPostList.as_view(), name='hashtag_list_posts'),
    
    # sitemap path
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]
