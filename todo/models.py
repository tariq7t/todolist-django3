from django.db import models
from django.contrib.auth.models import User


# Blank vs Null

class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    dateCompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    # Connecting with User table.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):

        return self.title