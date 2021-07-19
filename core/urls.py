from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('account/', include('accounts.urls', namespace='account')),
    path('p/', include('profiles.urls', namespace='profile')),
    path('auth', include('django.contrib.auth.urls')),
    path('skill/', include('skills.urls', namespace='skill')),
    path('sl/', include('social_links.urls', namespace='social_link')),
    path('l/', include('likes.urls', namespace='like')),
    path('c/', include('comments.urls', namespace='comment')),
    path('f/', include('favorite_post.urls', namespace='favorite')),

    # third party url
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
