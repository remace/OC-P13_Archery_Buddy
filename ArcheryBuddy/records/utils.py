from statistics import mean
from records.models import StatsRecord
from shapely import minimum_bounding_radius, distance as shapely_distance
from shapely.geometry import Polygon, Point


def calculate_barycentre(points: list[StatsRecord]) -> list[float, float]:

    if isinstance(points[0], StatsRecord):
        points_as_dicts = [
            {"arrow_id": point.arrow.pk,
             "pos_x": point.pos_x,
             "pos_y": point.pos_y}
            for point in points
        ]
    else:
        points_as_dicts = points

    list_x = [point.get("pos_x") for point in points_as_dicts]
    mean_x = mean(list_x)

    list_y = [point.get("pos_y") for point in points_as_dicts]
    mean_y = mean(list_y)

    return [round(mean_x, 2), round(mean_y, 2)]


def distance(point1, point2):
    return shapely_distance(
        Point(point1.get("pos_x"), point1.get("pos_y")),
        Point(point2.get("pos_x"), point2.get("pos_y")),
    )


def direction(point1, point2, point3):
    """returns perpendicular coordinate to p1p2 and p2p3 of the cross product:
    p1p2 ^ p2p3
    if p3 is "leftmost", it will be >0
    (attention: vertical axle is oriented to the bottom
                so cross product's sign is changed...
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
    """returns the convex hull (ordered)
    of a list of points (not necessarly ordered)
    uses Jarvis's march algorithm
    """
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
                and distance(prochain_2, current) > distance(prochain, current)
            ):
                prochain = prochain_2

        current = prochain
        if current == start:
            break
        result.append(prochain)
    return result


def calculate_quiver(points):
    """calculates the best quiver by
    excluding each round the worse grouping arrow:"""
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
            d0 = distance(points[2], points[0])
            + distance(points[0], points[1])
            d1 = distance(points[0], points[1])
            + distance(points[2], points[1])
            d2 = distance(points[2], points[1])
            + distance(points[2], points[0])

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
            circle_radiuses = []

            for point in points:
                # pour chaque point
                # on calcule le rayon du cercle circonscrit minimal
                # de l'envelope convexe "sans lui"
                points_without = points.copy()
                points_without.remove(point)
                hull = calculate_convex_hull(points_without)
                if len(hull) > 3:
                    radius = minimum_bounding_radius(
                        Polygon(
                            [(point.get("pos_x"), point.get("pos_y"))
                                for point in hull]
                        )
                    )
                else:
                    radius = 1000

                circle_radiuses.append(
                    {"arrow_id": point.get("arrow_id"), "radius": radius}
                )

            # on sélectionne celui qui est associé au
            # rayon de cercle circonscrit le plus petit
            min_radius_id = min(
                circle_radiuses, key=lambda arrow: arrow.get("radius")
            ).get("arrow_id")
            point_with_lower_radius = list(
                filter(lambda point: point.get("arrow_id")
                       == min_radius_id, points)
            )[0]

            # l'ajouter à la liste du resultat
            result.append(point_with_lower_radius)
            # la supprimer de points
            points.remove(point_with_lower_radius)

    # on renverse le résultat pour avoir les "meilleures flèches" en premier
    result.reverse()
    return result
