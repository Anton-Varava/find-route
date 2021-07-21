from trains.models import Train


def make_graph(queryset_trains):
    graph = {}
    for train in queryset_trains:
        graph.setdefault(train.from_city_id, set())
        graph[train.from_city_id].add(train.to_city_id)
    return graph


def get_all_ways(graph, from_city, to_city):
    queue_ = [(from_city, [from_city])]
    while queue_:
        (start, end) = queue_.pop()
        if start in graph.keys():
            for next_ in graph[start] - set(end):
                if next_ == to_city:
                    yield end + [next_]
                else:
                    queue_.append((next_, end + [next_]))


def find_fastest_way(ways: list):
    fastest_way = []
    fastest_time = None
    for way in ways:
        way_time = get_full_route_time(way)
        if not fastest_time or fastest_time > way_time:
            fastest_time = way_time
            fastest_way = way
    return fastest_way


def get_full_route_time(route):
    time = 0
    for i in range(len(route) - 1):
        trains = Train.objects.filter(from_city=route[i], to_city=route[i + 1])
        if len(trains) == 1:
            time += int(trains[0].travel_time)
        else:
            times = [int(train.travel_time) for train in trains]
            time += min(times)
    return time
