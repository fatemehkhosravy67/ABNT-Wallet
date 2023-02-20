from django.db import models


class Balance(models.Model):
    balance = models.BigIntegerField()


class Credit(models.Model):
    credit = models.CharField(max_length=256)


class Debit(models.Model):
    debit = models.CharField(max_length=256)
