# ArcheryBuddy - Note d'intention

## Les fonctionnalités attendues
Le but ici est de créer une application permettant une aide pour le tir à l'arc, selon 3 points:
1. Recenser le matériel et suivre l'état des flèches
2. Aider l'archer à choisir ses flèches pour une compétition future
3. Enregistrer des feuilles de score

## Recenser le matériel
Pour un archer qui a beaucoup de matériel, ou qui en change souvent, il n'a pas forcément en tête ses réglages. C'est là qu'une aide-mémoire peut être utile. L'idée pour cette fonctionnalité sera de pouvoir enregistrer à la fois le matériel et les réglages associés.

## Choisir les flèches
Un archer a généralement plus de flèches que nécessaire lorsqu'il s'engage dans une compétition. En général les compétitions nécessitent de tirer 3 ou 6 flèches par volée, donc les archers en choisissent 4 à 8 le jour de la compétition (pour pallier en cas de casse pendant la série), mais en utilisent régulièrement des lots de 6 à 12 pour les entrainements.

Chaque flèche a ses caractéristiques de vol, donc est légèrement différentes des autres. A tel point qu'avec un tir strictement identique deux flèches n'atterriront pas au même endroit en cible. Il faut donc, pour un archer, choisir celles qui sont le plus proches entre elles dans les conditions de la compétition à venir.

De plus, les flèches sont des objets relativement fragiles pour l'usage qui en est fait, et pouvoir noter qu'une flèche est à réparer est une fonctionnalité intéressante, et en tenir compte lors du calcul de ce "carquois optimal" est nécessaire.

## Saisir ses feuilles de score
En compétition, il n'est pas possible d'avoir un outil électronique. Toutefois, pour les entrainements, il est intéressant pour un archer de pouvoir suivre sa progression, à l'échelle d'une série, d'une compétition, ou même de la saison entière, notamment en conservant ses feuilles de score. L'idée sera donc d'implémenter cette fonctionnalité de sauvegarde.