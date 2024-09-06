from django.db import models
from wallet.models import Users


class Costs(models.Model):
    FREQ = [
        ('WR', "reminder"),
        ('ED', "every day"),
        ('EW', "every week"),
        ('EM', "every month"),
        ('EY', "every year"),
    ]

    title = models.CharField(max_length=40)
    owner = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='owners_costs') 
    recipient = models.ForeignKey(to=Users, on_delete=models.CASCADE, related_name='recipient_costs') 
    frequency = models.CharField(max_length=3, choices=FREQ, default='EM')
    price = models.DecimalField(max_digits=9, decimal_places=2)

