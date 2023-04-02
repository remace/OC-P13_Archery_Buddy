from math import sqrt
from statistics import mean
from records.models import StatsRecord
from shapely.geometry import Polygon

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
    # on prend le point d'abcisse la plus basse
    start = min(points, key=lambda point: point.get("pos_x"))

    # pour être sûr qu'il appartienne bien à l'enveloppe convexe:
    # on vérifie qu'il n'y en a pas d'ordonnée plus grande aussi,
    # et s'il y en a un, on change.
    for point in points:
        if start.get("pos_x") == point.get("pos_x"):
            if start.get("pos_y") < point.get("pos_y"):
                start = point

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
    return round(area, 1)


# def calculate_area(points):

#     # find a point in the middle of the polygon
#     mean_x, mean_y = calculate_barycentre(points)
#     barycentre = {"arrow_id": "barycentre", "pos_x": mean_x, "pos_y": mean_y}

#     total_area = 0
#     # accumulate areas of triangles
#     for point in points:
#         index = points.index(point)

#         try:
#             next_point = points[index + 1]
#         except IndexError:
#             next_point = points[0]

#         total_area += calculate_triangle_area(point, next_point, barycentre)

#     return total_area


def calculate_area(points):
    """calculate of the area using shoelace algorithm"""
    rearranged_points = [(point.get("pos_x"), point.get("pos_y")) for point in points]
    polygon = Polygon(rearranged_points)
    return polygon.area


def calculate_quiver(points):
    result = []
    while points != []:
        if len(points) < 2:
            return None

        elif len(points) == 2:
            result.append(points[0])
            result.append(points[1])
            points = []

        # s'il reste 3 points:
        elif len(points) == 3:
            d0 = distance(points[2], points[0]) + distance(points[0], points[1])
            d1 = distance(points[0], points[1]) + distance(points[2], points[1])
            d2 = distance(points[2], points[1]) + distance(points[2], points[0])

            if d0 > d1 and d0 > d2:
                # le point 0 est le "moins groupé"
                result.append(points[0])
                points.remove(points[0])
            if d1 > d0 and d1 > d2:
                # le point 1 est le moins groupé
                result.append(points[1])
                points.remove(points[1])
            if d2 > d1 and d2 > d0:
                # le point 2 est le moins groupé
                result.append(points[2])
                points.remove(points[2])

        else:
            areas = []
            # print("-----------------\nrésultat du tour de boucle:\npoints:")
            # pprint(points)
            for point in points:

                # print(f"point_enlevé: {point}")
                points_without = points.copy()
                points_without.remove(point)
                # pprint(points_without)
                hull = calculate_convex_hull(points_without)
                if len(hull) > 3:
                    area = calculate_area(hull)
                elif len(hull) == 3:
                    area = calculate_triangle_area(hull[0], hull[1], hull[2])
                else:
                    area = 0
                areas.append({"arrow_id": point.get("arrow_id"), "area": area})
            # print("areas:")
            # pprint(areas)
            # trouver l'aire minimale parmi areas
            min_area_id = min(areas, key=lambda arrow: arrow.get("area")).get(
                "arrow_id"
            )
            point_with_lower_area = list(
                filter(lambda point: point.get("arrow_id") == min_area_id, points)
            )[0]

            # print(
            #     f"donc l'aire la plus petite est celle de la flèche {point_with_lower_area.get('arrow_id')}"
            # )

            # l'ajouter à la liste du resultat
            result.append(point_with_lower_area)
            # la supprimer de points
            points.remove(point_with_lower_area)

            # print("qu'on va donc retirer des points, et ajouter au résultat:")
            # pprint(result)

    # on renverse le résultat pour avoir les "meilleures flèches" en premier
    result.reverse()
    return result
