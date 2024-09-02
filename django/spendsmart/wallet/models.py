from django.db import models

class Wallets(models.Model):
    owner = models.IntegerField(unique=True)
    invoice = models.DecimalField(max_digits=12, decimal_places=2)

class Users(models.Model):
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField()
    email = models.CharField(unique=True)
    
    def __str__(self):
        return str((self.pk, self.name, self.password, self.email))
 
