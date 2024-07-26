from django.contrib.auth.models import User
from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)
    position = models.IntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title
