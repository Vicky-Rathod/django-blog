from django.urls import path
from .views import FavoriteAddView, FavoriteList


app_name = 'favorite_post'
urlpatterns = [
     path('add-favorite/<slug>/', FavoriteAddView.as_view(), name='add_favorite_post_view'),
     path('favorite-list/', FavoriteList.as_view(), name='favorite_list_view'),
]
