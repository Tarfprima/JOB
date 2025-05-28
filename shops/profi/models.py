from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.CharField(max_length=1000)  
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name