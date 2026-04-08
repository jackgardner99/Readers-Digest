from django.db import models
from .book import Book
from django.contrib.auth.models import User

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True)
    comment = models.CharField(max_length=500)
    date_posted = models.CharField(max_length=10)
