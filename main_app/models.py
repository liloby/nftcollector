from django.db import models

# Create your models here.
class Nft(models.Model):
    name = models.CharField(max_length=100, null=True)
    collection_name = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.name