from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import Postform
class HomeView(View):
    template_name = 'index.html'
    def get(self, *args, **kwargs):
        object_list = Post.objects.all()
        context = {
            'object_list': object_list,
        }
        return render(self.request, self.template_name, context)

class AddPostView(LoginRequiredMixin, CreateView):
    template_name = 'add-post.html'
    form_class = Postform
    success_url = reverse_lazy('blog:home_view')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPostView, self).form_valid(form)