from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=100)
    website = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField("Author")
    publisher = models.ForeignKey('Publisher', on_delete = models.CASCADE)
    pubdate = models.DateField()

class Author(models.Model):
    name = models.CharField(max_length=50)
    intro = models.CharField(max_length=100)
    email = models.EmailField()