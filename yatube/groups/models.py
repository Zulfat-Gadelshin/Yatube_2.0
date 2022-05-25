from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True, )

    def __str__(self):
        return self.title
