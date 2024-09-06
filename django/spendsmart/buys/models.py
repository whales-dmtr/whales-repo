from django.db import models
from wallet.models import Users


class Buys(models.Model):
    title = models.CharField(max_length=40)
    owner = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)

