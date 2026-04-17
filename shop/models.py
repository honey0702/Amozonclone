from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.URLField()
    description = models.TextField()
    category = models.CharField(max_length=50, default='general') 

    def __str__(self):
        return self.name