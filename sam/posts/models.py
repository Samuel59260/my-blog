from django.db import models

# Create your models here.
class Articles(models.Model):
    nom = models.CharField(max_length=25)
    contenu = models.CharField(max_length=255)