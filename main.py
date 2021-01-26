def binary_search(arr: list, item: int) -> int:
    """
    Бинарный поиск ГЛАВА #1
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


# print(binary_search([1, 3, 5, 7, 9, 11], 3))


def find_smallest(arr: list) -> int:
    """
    Нахождение MIN списка
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr) - 1):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:
    """
    Сортировка Выбором ГЛАВА #2
    """
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


# print(selection_sort([11, 3, 15, 87, 9, -1, 11]))


def find_key_in_box(box: list) -> str:
    """
    Рекурсия поиск ключа в коробке
    key is 1
    Глава #3
    """
    for item in box:
        if item == 1:
            print("found the key!")
        elif type([]) is list:
            find_key_in_box(item)


# find_key_in_box([[], [], [[[1]]], [[]], []])


def quicksort(arr: list) -> list:
    """
    Быстрая сортировка Глава #4
    """
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


# print(quicksort([2, 4, 8, 1, 0]))


from collections import deque

graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy", "you"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name: str) -> bool:
    """"
    Поиск в ширину Глава #6
    """
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person[-1] == 'm':
                print(person + " is а mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


# print(search('you'))


def dijkstra_s(costs: dict) -> int:
    """
    Алгоритм Дейкстры Глава #7
    """
    node = find_lowest_cost_nod(costs)
    while node is not None:
        cost = costs[node]
        neighbors = _graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_nod(costs)
    return 'Кратчайший путь: {0}'.format(costs['fin'])


def find_lowest_cost_nod(costs: dict) -> str:
    """
    Нахождение Min веса в грфе
    """
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


_graph = dict()
_graph["start"] = {}
_graph["start"]["a"] = 6
_graph["start"]["b"] = 2
_graph["a"] = {}
_graph["a"]["fin"] = 1
_graph["b"] = {}
_graph["b"]["a"] = 3
_graph["b"]["fin"] = 5
_graph["fin"] = {}

costs = dict()
costs["a"] = 6
costs["b"] = 2
costs["fin"] = float("inf")

parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []


# print(dijkstra_s(costs))


def stations():
    """
    Жадный алгоритм Глава #8
    """
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "са", "az"}
    stations = dict()
    stations["kone"] = {"id", "nv", "ut"}
    stations["ktwo"] = {"wa", "id", "mt"}
    stations["kthree"] = {"or", "nv", "са"}
    stations["kfour"] = {"nv", "ut"}
    stations["kfive"] = {"ca", "az"}
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)
    return final_stations


# print(stations())
