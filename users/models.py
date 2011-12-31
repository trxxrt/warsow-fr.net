from django.db import models

# utilisateurs

class weapon(models.Model):
    full_name = models.CharField('nom complet', max_length=50)
    short_name = models.CharField('nom court', max_length=2)
    icon_path = models.CharField('chemin vers l\'icone', max_length=200)
    def __unicode__(self):
        return self.choice

class clan(models.Model):
    name = models.CharField('nom', max_length=50)
    email = models.CharField('email', max_length=200)
    is_playing_instagib = models.BooleanField('joue instagib')
    is_playing_nw = models.BooleanField('joue normal weapon')
    is_playing_race = models.BooleanField('joue race')
    password = models.CharField('mot de passe', max_length=200)
    def __unicode__(self):
        return self.choice

class player(models.Model):
    name = models.CharField('nom', max_length=200)
    first_name = models.CharField('prenom', max_length=200)
    pseudo = models.CharField('pseudo IG', max_length=200)
    email = models.CharField('email', max_length=200)
    is_playing_instagib = models.BooleanField('joue instagib')
    is_playing_nw = models.BooleanField('joue normal weapon')
    is_playing_race = models.BooleanField('joue race')
    password = models.CharField('mot de passe', max_length=200)
    birthday = models.DateTimeField('date de naissance')
    clan = models.ForeignKey(clan)
    def __unicode__(self):
        return self.choice
