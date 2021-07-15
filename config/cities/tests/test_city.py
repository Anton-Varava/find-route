from django.test import TestCase
from cities.models import City
from django.shortcuts import get_list_or_404


class CitiesListTestCase(TestCase):
    def setUp(self) -> None:
        city_1 = City.objects.create(title='Kharkiv')
        city_2 = City.objects.create(title='Poltava')

    def test_get(self):
        city_1 = City.objects.get(id=1)
        city_2 = City.objects.get(id=2)

        self.assertEqual('Kharkiv1', city_1.__str__())
        self.assertEqual('Poltava', city_2.__str__())
        self.assertEqual(2, City.objects.all().count())

    def test_add_new_city(self):
        pass

