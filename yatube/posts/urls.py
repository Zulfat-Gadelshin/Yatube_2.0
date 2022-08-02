from django.urls import path
from . import views

app_name = 'post_url'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('profile/<str:username>/posts/', views.users_posts, name='users_posts'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/new_post/', views.new_post, name='new_post'),
    path('posts/<int:post_id>/edit', views.post_edit, name='post_edit'),
]
