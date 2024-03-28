from geopy.distance import geodesic


def calculate_distance(point1, point2):
    """
    Функция для вычисления расстояния между двумя географическими точками.
    point1 и point2 должны быть кортежами в формате (широта, долгота).
    """

    distance = geodesic(point1, point2).miles
    return distance
