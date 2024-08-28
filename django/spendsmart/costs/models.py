from django.db import models

class Costs(models.Model):
    title = models.CharField(max_length=40)
    price = models.FloatField(max_length=11)
    time_create = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=6)
 