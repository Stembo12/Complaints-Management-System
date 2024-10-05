from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=254)
    city = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name
    