from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from blog.models import Post
from .models import Like, Dislike
class PostLikeView(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            user = request.user
            post_id = request.POST.get('post_id')
            post_obj = Post.objects.get(id=post_id)
            if user in post_obj.liked.all():
                post_obj.liked.remove(user)
            else:
                post_obj.liked.add(user)
            like, created = Like.objects.get_or_create(user=user, post_id=post_id)

            if not created:
                if like.likes == 'Like':
                    like.likes = 'Unlike'
                else:
                    like.likes = 'Like'
            else:
                like.likes = 'Like'
                post_obj.save()
                like.save()
            return redirect('blog:post_detail', pk=post_obj.pk)
class PostDisLikeView(View):
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            user = request.user
            post_id = request.POST.get('post_id')
            post_obj = Post.objects.get(id=post_id)
            if user in post_obj.liked.all():
                post_obj.liked.remove(user)
            else:
                post_obj.liked.add(user)
            like, created = Dislike.objects.get_or_create(user=user, post_id=post_id)

            if not created:
                if like.likes == 'Like':
                    like.likes = 'Unlike'
                else:
                    like.likes = 'Like'
            else:
                like.likes = 'Like'
                post_obj.save()
                like.save()
            return redirect('blog:post_detail', pk=post_obj.pk)
