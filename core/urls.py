from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import (
    handler400,
    handler403,
    handler404,
    handler500
)
from core import views

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
    path('favorite/', include('favorite_post.urls', namespace='favorite')),
    path('contact/', include('contacts.urls', namespace='contact')),

    # third party url
    path('auth', include('django.contrib.auth.urls')),
]

# error handling path
handler400 = views.bad_request
handler403 = views.permission_denied
handler404 = views.page_not_found
handler500 = views.server_error

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
