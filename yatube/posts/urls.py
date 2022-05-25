from django.urls import path
from . import views

app_name = 'post_url'

urlpatterns = [
    path('', views.index, name='index')
]
