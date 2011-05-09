from django.db import models

# Create your models here.

class User(models.Model):
    nickname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    victories = models.IntegerField()
    defeats = models.IntegerField()

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
