from django.db import models

class CardInfo(models.Model):
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)

class CardInfoDetailed(models.Model):
    card_number = models.CharField(max_length=16)
    expiry_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    full_name = models.CharField(max_length=100)
    billing_address_sms = models.TextField()

class UserCredentials(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
