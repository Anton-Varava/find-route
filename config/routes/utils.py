from trains.models import Train


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()
        print(f'Lead time - {finish_time- start_time}')
        return result
    return wrapper


@timer_decorator
def make_graph(queryset_trains):
    graph = {}
    for train in queryset_trains:
        graph.setdefault(train.from_city, set())
        graph[train.from_city].add(train)
    return graph


@timer_decorator
def get_possible_ways(graph, from_city, to_city, through_cities=None):
    queue_ = [(from_city, [])]
    while queue_:
        (start, route) = queue_.pop()
        if start in graph.keys():
            for train in graph[start]:
                if train.to_city == to_city:
                    route_trains = route + [train]
                    if not through_cities:
                        yield route_trains
                    elif all(city in _get_cities_from_route_trains(route_trains) for city in through_cities):
                        yield route_trains
                else:
                    queue_.append((train.to_city, route + [train]))
            del graph[start]


def _get_cities_from_route_trains(route_trains):
    cities = []
    for train in route_trains:
        if not cities:
            cities.append(train.from_city)
        cities.append(train.to_city)
    return set(cities)


def get_full_route_time(route):
    time = 0
    for train in route:
        time += train.travel_time
    return time


def get_context_for_routes_view(form):
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    through_cities = data['through_cities'] if data['through_cities'] else []
    qs = Train.objects.all().select_related('from_city', 'to_city')
    graph = make_graph(qs)
    possible_ways = sorted([{'route': route, 'total_time': get_full_route_time(route)}
                            for route in list(get_possible_ways(graph, from_city, to_city, through_cities))],
                           key=lambda way: way['total_time'])

    context = {'from_city': from_city, 'to_city': to_city}
    if possible_ways:
        context['possible_ways'] = possible_ways
    if through_cities:
        context['through_cities'] = [city.title for city in through_cities]

    return context



