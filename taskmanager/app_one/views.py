from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.draft.all()
    return render(request, 'app_one/post/list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.DRAFT)
    return render(request, 'app_one/post/detail.html', {'post': post})
