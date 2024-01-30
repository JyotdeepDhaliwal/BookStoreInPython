from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.title
