from django.db import models


# Create your models here.
class City(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['title']

