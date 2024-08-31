from django.db import models

class Buys(models.Model):
    title = models.CharField(max_length=40)
    owner = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)


