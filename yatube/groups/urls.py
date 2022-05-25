from django.urls import path
from . import views

app_name = 'group_url'

urlpatterns = [
    path('<slug:slug>/', views.groups_posts, name='group_posts'),
]
