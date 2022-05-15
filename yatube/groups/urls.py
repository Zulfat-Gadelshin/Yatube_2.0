from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.groups_posts),
]
