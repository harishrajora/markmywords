from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class WordMeaning(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.ForeignKey(User, to_field = "username", on_delete = models.CASCADE)
    word = models.CharField(max_length = 100, default = "Null12")
    meaning = models.TextField()


class UserTable(models.Model):
    username = models.ForeignKey(User, to_field = "username", on_delete = models.CASCADE)
    list_of_words = models.TextField()
