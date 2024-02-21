# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Paragraph(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()

    def __str__(self):
        return self.text[:50]

class Word(models.Model):
    word = models.CharField(max_length=50)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)

    def __str__(self):
        return self.word
    
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
