from django.db import models

# Create your models here.

class Email(models.Model):
    email =  email = models.EmailField(unique=True)
