from django.db import models

# utilisateurs

class clan(models.Model):
    name = models.CharField('nom', max_length=50)
    email = models.CharField('email', max_length=200)
    password = models.CharField('mot de passe', max_length=200)
    def __unicode__(self):
        return self.choice


class player(models.Model):
    name = models.CharField('nom', max_length=200)
    email = models.CharField('email', max_length=200)
    password = models.CharField('mot de passe', max_length=200)
    birthday = models.DateTimeField('date de naissance')
    clan = models.ForeignKey(clan)
    def __unicode__(self):
        return self.choice
