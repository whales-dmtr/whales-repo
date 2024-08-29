from django.db import models

class Costs(models.Model):
    FREQ = [
        # (range(1, 365), "custom number of days")
        ('ND', "custom number of days"),
        ('ED', "every day"),
        ('EW', "every week"),
        ('EM', "every month"),
        ('EY', "every year"),
    ]

    title = models.CharField(max_length=40)
    owner = models.IntegerField()  # после создания таблицы юзеров сделать внешним ключом
    recipient = models.IntegerField()  
    frequency = models.CharField(max_length=3, choices=FREQ, default='EM')
    price = models.DecimalField(max_digits=9, decimal_places=2)


