from django.shortcuts import render
from .models import Post


def index(request):
    template = 'posts/index.html'

    posts = Post.objects.order_by('-pub_date')[:10]

    context = {
        'posts': posts,
    }
    return render(request, template, context)
