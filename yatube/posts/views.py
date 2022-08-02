from django.shortcuts import render
from .models import Post
from groups.models import Group
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, get_list_or_404
from .forms import NewPostForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

User = get_user_model()


def index(request):
    template = 'posts/index.html'
    post_list = Post.objects.all().order_by('-pub_date')
    posts = Post.objects.order_by('-pub_date')
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = get_list_or_404(Post, author=user)
    # paginator = Paginator(posts, 10)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    context = {
        'cur_user': user,
        'posts': posts,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user_posts_count = Post.objects.filter(author=post.author).count()
    context = {
        'post': post,
        'user_posts_count': user_posts_count,
    }
    return render(request, 'posts/post_detail.html', context)


def users_posts(request, username):
    user = get_object_or_404(User, username=username)
    posts = get_list_or_404(Post, author=user)
    context = {
        'cur_user': user,
        'posts': posts,
    }
    return render(request, 'posts/users_posts.html', context)



@login_required
def new_post(request):
    user = request.user
    groups = Group.objects.filter(author=user)
    form = NewPostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect(reverse_lazy('post_url:index'))
    return render(request, 'posts/new_post.html', {'form': form, 'groups': groups,})


@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    author = get_object_or_404(User, username=post.author)
    user = request.user
    if user == author:
        groups = Group.objects.filter(author=user)
        form = NewPostForm(instance=post)
        if request.method == 'POST':
            form = NewPostForm(request.POST or None)
            if form.is_valid():
                post.text = form.cleaned_data['text']
                post.group = form.cleaned_data['group']
                post.save()
                return redirect('post_url:post_detail', post_id=post_id)
        return render(request, 'posts/new_post.html',
                          {'form': form, 'groups': groups, 'for_edit': True, 'post_id': post.pk})
    return redirect('post_url:post_detail',  post_id=post_id)
