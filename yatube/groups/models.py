from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group'
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True, )

    def __str__(self):
        return self.title
