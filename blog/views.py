from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post
from .forms import Postform

class HomeView(View):
    template_name = 'index.html'
    def get(self, *args, **kwargs):
        object_list = Post.post_manager.all()
        context = {
            'object_list': object_list,
        }
        return render(self.request, self.template_name, context)
    
class SinglePostView(DetailView):
    model = Post
    template_name = 'single.html'

class SingePostDeleteView(LoginRequiredMixin, DeleteView):
    # specify the model you want to use
    model = Post
     
    # can specify success url
    # url to redirect after successfully
    # deleting object
    success_url = "/"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)

class AddPostView(LoginRequiredMixin, CreateView):
    template_name = 'add-post.html'
    form_class = Postform
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPostView, self).form_valid(form)
 
class PostUpdateView(LoginRequiredMixin, UpdateView):
    # specify the model you want to use
    model = Post
    template_name = 'update-post.html'
    form_class = Postform
    success_url = '/'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != self.request.user:
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostUpdateView, self).form_valid(form)

class PostLikeView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        user = request.user
        post = Post.objects.get(pk=pk)

        # Post DisLike Button
        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == user:
                is_dislike = True
                break
        
        if is_dislike:
            post.dislikes.remove(user)

        # Post Like Button
        is_like = False

        for like in post.likes.all():
            if like == user:
                is_like = True
                break
        
        if not is_like:
            post.likes.add(user)
        if is_like:
            post.likes.remove(user)
        
        # next = request.POST.get('next', '/')
        next = request.META['HTTP_REFERER']
        return HttpResponseRedirect(next)
class PostDisLikeView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        user = request.user
        post = Post.objects.get(pk=pk)

        # Post DisLike Button
        is_like = False

        for like in post.likes.all():
            if like == user:
                is_like = True
                break
        if is_like:
            post.likes.remove(user)
        
        # Post DisLike Button
        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == user:
                is_dislike = True
                break
        
        if not is_dislike:
            post.dislikes.add(user)

        if is_dislike:
            post.dislikes.remove(user)
        
        # next = request.POST.get('next', '/')
        next = request.META['HTTP_REFERER']
        return HttpResponseRedirect(next)