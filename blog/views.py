from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import View, ListView, DetailView, CreateView
from .models import Post

class HomeView(View):
    template_name = 'index.html'
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

class AddPostView(CreateView):
    model = Post
    fields = ('title', 'description')
    template_name = 'add-post.html'

    def form_valid(self)
