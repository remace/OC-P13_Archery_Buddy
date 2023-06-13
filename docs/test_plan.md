# Plan de tests

## tests unitaires
- Les objets du modèle et leurs interactions simples avec une Base de données: sauvegarde, lecture, modification, suppression.

_par exemple: tester que le UserManager crée bien un unique utilisateur conforme aux données qui lui sont fournies._

## tests fonctionnels
- test du fonctionnement d'une fonctionnalité complète selon les cas d'usage: 

_par exemple: tester que la vue d'enregistrement d'utilisateur renvoie bien le bon statut HTTP, et redirige bien vers la homepage._

## tests d'intégration

- test d'une fonctionnalité "comme si l'utilisateur le faisait vraiment dans un navigateur"

_par exemple: au logout, vérifier que l'affichage de la barre de menu affiche bien le bouton "se connecter" au lieu du bouton "profil"._

- tester les fonctionnalités qui seront exécutées "côté client"

_par exemple: tester un changement de automatique couleur d'arrière plan de champ de texte dans une vue._