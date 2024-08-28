from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
class Costs(models.Model):
    title = models.CharField(max_length=40)
    price = models.FloatField(max_length=11)
    time_create = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=6)
 
>>>>>>> 18f0a2e (Add conection to PostgreSQL DB)
