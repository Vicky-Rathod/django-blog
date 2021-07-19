from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from .models import Comment
class CommentCreateView(CreateView):
    model = Comment
    fields = ('content',)

    # def get(self, request):
    #     next = request.POST.get('next', '/')
    #     return HttpResponseRedirect(next)
    # def get_success_url(self):
    #     return reverse_lazy('blog:single_post_view', kwargs={'slug':self.object.post.slug})

    def form_valid(self, form):
        form.instance.post = Post.objects.get(slug=self.kwargs.get("slug"))
        form.instance.user = self.request.user
        print(form.instance)
        return super(CommentCreateView, self).form_valid(form)

    # def form_valid(self, form):
    #     form.instance.post_id = self.kwargs['pk']
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

