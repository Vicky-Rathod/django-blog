from django.urls import path
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from .views import (
    HomeView,
    AddPostView,
)

sitemaps = {
    "posts": PostSitemap,
}

app_name = 'blog'
urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('add-post/', AddPostView.as_view(), name='add_post_view'),
    
    # sitemap path
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]
