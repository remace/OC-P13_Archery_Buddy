from statistics import mean
from records.models import StatsRecord


def calculate_barycentre(points: list[StatsRecord]) -> list[float, float]:

    list_x = [point.pos_x for point in points]
    mean_x = mean(list_x)

    list_y = [point.pos_y for point in points]
    mean_y = mean(list_y)

    return [mean_x, mean_y]


def squared_distance(point_1, point_2):
    dx, dy = point_1.pos_x - point_2.pos_x, point_1.pos_y - point_2.pos_y
    return dx**2 + dy**2



def calculate_quiver(points):
    # si il y a 2 points ou moins
    # ça n'a aucun sens d'essayer de compter
    if len(points <= 2):
        return points
    # s'il reste 3 points:
    if len(points == 3):
        d0 = distance(points[2], points[0]) + distance(points[0], points[1])
        d1 = distance(points[0], points[1]) + distance(points[2], points[1])
        d2 = distance(points[2], points[1]) + distance(points[2], points[0])

        if d0 > d1 and d0 > d2:
            # le point 0 est le "moins groupé"
            return calculate_quiver(points[1], points[2]), points[0]
        if d1 > d0 and d1 > d2:
            # le point 1 est le moins groupé
            return calculate_quiver(points[0], points[2]), points[1]
        if d2 > d1 and d2 > d0:
            # le point 2 est le oins groupé
            return calculate_quiver(points[1], points[0]), points[2]

    else:
        pass
    # s'il en reste plus:
    #   - calculer l'enveloppe convexe de la récursion et son aire
    #     (possibilité de la récupérer de la récursion précédente?)
    #   - calculer l'enveloppe convexe "sans chaque point" et leurs aires
    #   - trier par envelope convexe croissante
    #   - retourner [calculate_quiver(la liste sans le point qui donne l'envelope convexe la plus grande), x ] # x étant le point sans lequel l'envelope diminue le plus
    #     (étudier si besoin la possibilité de refiler l'envelope et son aire à la récursion suivante)
