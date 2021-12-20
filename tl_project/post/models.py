from django.db import models
from django.utils import timezone
from members.models import Member


class Post(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return '{}'.format(self.title)


