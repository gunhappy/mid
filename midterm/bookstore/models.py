from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.PositiveIntegerField(primary_key=True)
    ISBN = models.CharField(max_length=6)
    book_name = models.CharField(max_length=50)
    price =  models.IntegerField(default=0)
    author = models.CharField(max_length=50)
