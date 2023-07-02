from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    price = models.FloatField()
    title = models.CharField(max_length=155)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    message = models.TextField()

    def __str__(self):
        return self.name
