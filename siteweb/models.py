from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    message = models.TextField()
    
    
class Categorie_Service(models.Model):
    libelle = models.CharField(max_length=100)
    
    
class Service(models.Model):
    titre = models.CharField(max_length=200, null=True)
    detail = models.TextField()
    image = models.ImageField(upload_to='uploads', default='uploads/img.png')
    

    
class Fonctionalite(models.Model):
    libelle = models.CharField(max_length=200, null=True)


class Application(models.Model):
    titre = models.CharField(max_length=200, null=True)
    demo = models.TextField()
    Fonctionalite = models.ForeignKey(Fonctionalite, on_delete=models.CASCADE)
    
    
class Atualite(models.Model):
    titre = models.CharField(max_length=200, null=True)
    contenu = models.TextField()
    date_mise_ligne = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads', default='uploads/img.png')
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    