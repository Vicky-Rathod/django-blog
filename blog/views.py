from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView
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