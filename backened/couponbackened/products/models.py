from django.db import models

class ProductDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100, default="Null", blank=True)
    price = models.CharField(max_length=100, default=0)

    def __str__(self):
        return f"{self.name}"