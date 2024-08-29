from django.db import models

class Costs(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=40)
    price = models.FloatField(max_length=11)
    time_create = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=6)
 
=======
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


>>>>>>> main
