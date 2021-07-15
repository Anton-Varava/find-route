from django.db import models
from cities.models import City


# Create your models here.
class Train(models.Model):
    number = models.CharField(max_length=10, unique=True)
    travel_time = models.PositiveSmallIntegerField(verbose_name='Travel time')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Departure city',
                                  related_name='from_city_set')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Arrival city',
                                related_name='to_city_set')

    def __str__(self):
        return f'Train №{self.number} {self.from_city}-{self.to_city}'





