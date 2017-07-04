from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_list(request):
    posts = Post.objects.order_by('-title')
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)


def blog_single_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/single_post.html', {'post': post})

