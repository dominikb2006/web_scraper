from django.db import models


class Address(models.Model):
    address_ID = models.AutoField(primary_key=True)
    address_city = models.CharField(max_length=128)
    address_ZIP = models.DecimalField(max_length=10)
    address_street = models.CharField(max_length=128)
    address_number = models.CharField(max_length=64)

    def __str__(self):
        return str(self.address_city + ", " + self.address_ZIP + ", " + self.address_street + " " + self.address_number)


class Card(models.Model):
    card_ID = models.AutoField(primary_key=True)
    card_number = models.DecimalField(max_length=16)
    card_date = models.DateField()
    card_CVV = models.DecimalField(max_length=3)

    def __str__(self):
        return str(self.card_number)


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    # address = models.ForeignKey(Address, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=16, unique=True)
    email = models.EmailField(max_length=128, unique=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
