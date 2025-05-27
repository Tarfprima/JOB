from django.db import models
from datetime import datetime

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    timer = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name