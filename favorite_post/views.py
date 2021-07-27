from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from blog.models import Post

class FavoriteList(LoginRequiredMixin, View):
    template_name = 'post/favorite-list.html'
    def get(self, request, *args, **kwargs):
        favorite = Post.post_manager.filter(favorites=request.user)
        return render(request, self.template_name, {'favorite_list': favorite})
class FavoriteAddView(LoginRequiredMixin, View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        if post.favorites.filter(id=request.user.pk).exists():
            post.favorites.remove(request.user)
        else:
            post.favorites.add(request.user)
        next = request.META['HTTP_REFERER']
        return HttpResponseRedirect(next)
