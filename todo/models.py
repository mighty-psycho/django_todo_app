from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=250, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
