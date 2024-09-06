from django.db import models


class UnblockUsersManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_blocked=False)


class Users(models.Model):
    name = models.CharField(max_length=20, unique=True)
    password = models.CharField()
    email = models.EmailField(unique=True)
    status = models.CharField(default='user')
    is_blocked = models.BooleanField(default=False)
    
    objects = models.Manager()
    unblock_users = UnblockUsersManager()

    def __str__(self):
        return self.name

class Wallets(models.Model):
    owner = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    invoice = models.DecimalField(max_digits=12, decimal_places=2)

