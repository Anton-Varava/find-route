from trains.models import Train


def make_graph(queryset_trains):
    graph = {}
    for train in queryset_trains:
        graph.setdefault(train.from_city, set())
        graph[train.from_city].add(train)
    return graph


def get_possible_ways(graph, from_city, to_city):
    queue_ = [(from_city, [])]
    while queue_:
        (start, route) = queue_.pop()
        if start in graph.keys():
            for train in graph[start]:
                if train.to_city == to_city:
                    yield route + [train]
                else:
                    queue_.append((train.to_city, route + [train]))


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
    qs = Train.objects.all()
    graph = make_graph(qs)
    possible_ways = sorted(list(get_possible_ways(graph, from_city, to_city)), key=get_full_route_time)
    context = {'from_city': from_city, 'to_city': to_city, 'possible_ways': possible_ways}
    return context

