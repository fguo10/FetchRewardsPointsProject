from django.db import models

# Create your models here.
from django.db.models import Sum


class Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    payer = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    unused_points = models.IntegerField(default=0)
    timestamp = models.DateTimeField(null=False)
    is_credit = models.BooleanField(default=True)

    def __str__(self):
        return f'Transaction: payer={self.payer}, points={self.points}'
