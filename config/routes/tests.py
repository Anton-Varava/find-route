from django.test import TestCase
from trains.models import Train
from cities.models import City
from .utils import make_graph, get_all_ways, find_fastest_way


# Create your tests here.
class RoutesTestCase(TestCase):
    def setUp(self):
        kharkiv = City.objects.create(title='kharkiv')
        poltava = City.objects.create(title='Poltava')
        kiyv = City.objects.create(title='Kiyv')
        dnipro = City.objects.create(title='Dnipro')

        kharkiv_potava = Train.objects.create(number='11', travel_time=2,
                                              from_city=kharkiv,
                                              to_city=poltava)
        poltava_kiyv = Train.objects.create(number='22', travel_time=3,
                                            from_city=poltava,
                                            to_city=kiyv)
        kharkiv_dnipro = Train.objects.create(number='33', travel_time=4,
                                              from_city=kharkiv,
                                              to_city=dnipro)
        dnipro_kiyv = Train.objects.create(number='44', travel_time=6,
                                           from_city=dnipro,
                                           to_city=kiyv)

    def test_find_way(self):
        graph = make_graph(Train.objects.all())
        all_ways = list(get_all_ways(graph=graph, from_city=1, to_city=3))

        self.assertEqual(2, len(all_ways))
        self.assertEqual(True, ([1, 2, 3] in all_ways))
        self.assertEqual(True, ([1, 4, 3] in all_ways))

    def test_find_fastest_way(self):
        graph = make_graph(Train.objects.all())
        all_ways = list(get_all_ways(graph=graph, from_city=1, to_city=3))
        self.assertEqual([1, 4, 3], find_fastest_way(all_ways))
