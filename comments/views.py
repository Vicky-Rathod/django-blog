from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from .models import Comment
from .forms import CreateCommentForm

class CommentCreateView(CreateView):
    model = Comment
    form_class = CreateCommentForm

    def form_valid(self, form):
        post = Post.objects.get(slug=self.kwargs.get("slug"))
        form.instance.post = post
        form.instance.user = self.request.user
        return super(CommentCreateView, self).form_valid(form)

