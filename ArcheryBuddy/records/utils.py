from statistics import mean
from records.models import StatsRecord


def calculate_barycentre(points: list[StatsRecord]) -> list[float, float]:

    list_x = [point.pos_x for point in points]
    mean_x = mean(list_x)

    list_y = [point.pos_y for point in points]
    mean_y = mean(list_y)

    return [mean_x, mean_y]
