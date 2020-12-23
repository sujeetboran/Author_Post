from django.db import models
from uuid import uuid4


# Create your models here.
class User(models.Model):
    username = models.CharField(primary_key=True, max_length=50, unique=True)
    password = models.CharField(max_length=50)


class authors(models.Model):
    ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=10, null=False)
    posts = models.IntegerField(null=False, default=0)


class post(models.Model):
    # we can use default UUID as a primary key for example
    # this :- ID          = models.UUIDField(primary_key=True, default=uuid4, null=False)
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    # author = models.ForeignKey(authors, on_delete=models.CASCADE)
    author = models.CharField(max_length=50, null=False)
    views = models.IntegerField(null=False, default=0)
    reviews = models.IntegerField(null=False, default=0)
