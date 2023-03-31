from math import sqrt
from statistics import mean
from records.models import StatsRecord

from pprint import pprint


def calculate_barycentre(points: list[StatsRecord]) -> list[float, float]:

    if isinstance(points[0], StatsRecord):
        points_as_dicts = [
            {"arrow_id": point.arrow.pk, "pos_x": point.pos_x, "pos_y": point.pos_y}
            for point in points
        ]
    else:
        points_as_dicts = points

    list_x = [point.get("pos_x") for point in points_as_dicts]
    mean_x = mean(list_x)

    list_y = [point.get("pos_y") for point in points_as_dicts]
    mean_y = mean(list_y)

    return [round(mean_x, 2), round(mean_y, 2)]


def squared_distance(point1, point2):

    dx, dy = point1.get("pos_x") - point2.get("pos_x"), point1.get(
        "pos_y"
    ) - point2.get("pos_y")
    return round(dx**2 + dy**2, 2)


def distance(point1, point2):
    return round(squared_distance(point1, point2) ** 0.5, 2)


def direction(point1, point2, point3):
    """retourne la composante perpendiculaire à p1p2 et p2p3 du produit vectoriel suivant:
    p1p2 ^ p2p3
    si p3 est "plus à gauche que p2", la composante sera positive
    (bête rappel: l'axe des ordonnées pointe vers le bas donc:
        le signe du produit vectoriel est changé par rapport à d'habitude
    )
    """

    vecteur12 = (
        point2.get("pos_x") - point1.get("pos_x"),
        point2.get("pos_y") - point1.get("pos_y"),
    )
    vecteur23 = (
        point3.get("pos_x") - point2.get("pos_x"),
        point3.get("pos_y") - point2.get("pos_y"),
    )

    return round(vecteur12[0] * vecteur23[1] - vecteur12[1] * vecteur23[0], 2)


def calculate_convex_hull(points):
    start = min(points, key=lambda point: point.get("pos_x"))
    current = start
    result = []
    result.append(start)

    while True:
        prochain = points[1] if points[0] != current else points[0]
        for prochain_2 in points:
            if prochain_2 == prochain:
                continue

            angle = direction(current, prochain, prochain_2)

            if angle > 0 or (
                angle == 0
                and squared_distance(prochain_2, current)
                > squared_distance(prochain, current)
            ):
                prochain = prochain_2

        current = prochain
        if current == start:
            break
        result.append(prochain)
    return result


def calculate_triangle_area(point1, point2, point3):

    a = distance(point1, point2)
    b = distance(point2, point3)
    c = distance(point3, point1)
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return round(area, 2)


def calculate_area(points):

    # find a point in the middle of the polygon
    mean_x, mean_y = calculate_barycentre(points)
    barycentre = {"arrow_id": "barycentre", "pos_x": mean_x, "pos_y": mean_y}

    total_area = 0
    # accumulate areas of triangles
    for point in points:
        index = points.index(point)

        try:
            next_point = points[index + 1]
        except IndexError:
            next_point = points[0]

        total_area += calculate_triangle_area(point, next_point, barycentre)

    return round(total_area, 1)


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
