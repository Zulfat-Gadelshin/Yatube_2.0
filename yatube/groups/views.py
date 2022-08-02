from django.shortcuts import render, get_object_or_404
from .models import Group
from django.core.paginator import Paginator


def groups_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    posts = group.posts.order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'group': group,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)
