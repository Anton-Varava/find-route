from django.test import TestCase
from django.core.exceptions import ValidationError

from trains.models import Train
from cities.models import City


# Create your tests here.
class TrainCreateTest(TestCase):
    def test_create_validation(self):
        with self.assertRaises(ValidationError):
            city = City.objects.create(title='Poltava')
            new_train = Train(number='111', travel_time=2, from_city=city, to_city=city)
            new_train.full_clean()

