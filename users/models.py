from django.db import models


class User(models.Model):

    class Meta:
        ordering = ['-name']

    name = models.CharField(max_length=254)
    contractor = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    supervisor = models.BooleanField( )
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.name

