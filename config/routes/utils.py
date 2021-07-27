from trains.models import Train


def make_graph(queryset_trains):
    graph = {}
    for train in queryset_trains:
        graph.setdefault(train.from_city, set())
        graph[train.from_city].add(train)
    return graph


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


def _get_cities_from_route_trains(route_trains):
    cities = []
    for train in route_trains:
        if not cities:
            cities.append(train.from_city)
        cities.append(train.to_city)
    return set(cities)


def find_fastest_way(routes: list):
    fastest_way = {'fastest_time': None, 'fastest_route': []}
    for route in routes:
        way_time = get_full_route_time(route)
        if not fastest_way['fastest_time'] or fastest_way['fastest_time'] > way_time:
            fastest_way['fastest_time'] = way_time
            fastest_way['fastest_route'] = route
    return fastest_way


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
    qs = Train.objects.all()
    graph = make_graph(qs)
    possible_ways = sorted(list(get_possible_ways(graph, from_city, to_city, through_cities)), key=get_full_route_time)

    context = {'from_city': from_city, 'to_city': to_city}
    if possible_ways:
        context['possible_ways'] = possible_ways
    if through_cities:
        context['through_cities'] = [city.title for city in through_cities]

    return context

