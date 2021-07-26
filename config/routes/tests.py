from django.test import TestCase
from trains.models import Train
from cities.models import City
from .utils import make_graph, get_possible_ways, find_fastest_way


# Create your tests here.
class RoutesTestCase(TestCase):
    __kharkiv_id = 1
    __kiev_id = 3

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

    @staticmethod
    def __get_ways(from_city=__kharkiv_id, to_city=__kiev_id):
        graph = make_graph(Train.objects.all())
        all_ways = list(get_possible_ways(graph=graph, from_city=from_city, to_city=to_city))
        return all_ways

    @staticmethod
    def __get_train_object_by_id(_id):
        return Train.objects.get(id=_id)

    @staticmethod
    def __get_city_object_by_id(_id):
        return City.objects.get(id=_id)

    def test_find_way(self):
        all_ways = RoutesTestCase.__get_ways(
            from_city=RoutesTestCase.__get_city_object_by_id(RoutesTestCase.__kharkiv_id),
            to_city=RoutesTestCase.__get_city_object_by_id(RoutesTestCase.__kiev_id))
        k_p = RoutesTestCase.__get_train_object_by_id(_id=1)
        p_k = RoutesTestCase.__get_train_object_by_id(_id=2)
        k_d = RoutesTestCase.__get_train_object_by_id(_id=3)
        d_k = RoutesTestCase.__get_train_object_by_id(_id=4)

        self.assertEqual(2, len(all_ways))
        self.assertEqual(True, ([k_p, p_k] in all_ways))
        self.assertEqual(True, ([k_d, d_k] in all_ways))

    def test_find_fastest_way(self):
        all_ways = RoutesTestCase.__get_ways(
            from_city=RoutesTestCase.__get_city_object_by_id(RoutesTestCase.__kharkiv_id),
            to_city=RoutesTestCase.__get_city_object_by_id(RoutesTestCase.__kiev_id))
        k_p = RoutesTestCase.__get_train_object_by_id(_id=1)
        p_k = RoutesTestCase.__get_train_object_by_id(_id=2)
        self.assertEqual([k_p, p_k], find_fastest_way(all_ways)['fastest_route'])
        self.assertEqual(5, find_fastest_way(all_ways)['fastest_time'])
