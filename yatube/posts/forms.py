from django import forms
from .models import Post
from groups.models import Group


class NewPostForm(forms.ModelForm):


    class Meta:
        # На основе какой модели создаётся класс формы
        model = Post
        # Укажем, какие поля будут в форме
        fields = ('text', 'group')

