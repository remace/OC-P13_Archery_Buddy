## Package Quiver
### UC-2 - saisir les données des flèches

<table>
    <tbody>
        <tr>
            <td>
                Acteurs Concernés
            </td>
            <td>
                Utilisateur connecté
            </td>
        </tr>
        <tr>
            <td>
                Description
            </td>
            <td>
                permet à l'utilisateur de saisir les données de ses flèches (position des tirs)
            </td>
        </tr>
        <tr>
            <td>
                Date
            </td>
            <td>
                17/05/2022
            </td>
        </tr>
        <tr>
            <td>
                Auteur
            </td>
            <td>
                Rémi TAUVEL
            </td>
        </tr>
        <tr>
            <td>
                Pré-conditions
            </td>
            <td>
                Utilisateur connecté
            </td>
        </tr>
        <tr>
            <td>
                Démarrage
            </td>
            <td>
                page d'enregistrement des flèches
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <strong>Dialogue</strong>
            </td>
        </tr>
        <tr>
            <td>
                Scénario nominal
            </td>
            <td>
              <ol>
                  <li>
                  <strong>L'utilisateur</strong> crée une volée
                  </li>
                  <li>
                  <em>Le système</em> lui affiche les champs nécessaires
                  </li>
                  <li>
                    <strong>L'utilisateur</strong> tire ses flèches et les saisit
                  </li>
                  <li>
                    recommencer jusqu'à ce que <strong>l'utilisateur</strong> demande la fin de l'enregistrement
                  </li>                  
              </ol>
            </td>
        </tr>
        <tr>
            <td>
                Scénario alternatif
            </td>
            <td>
              <ul style="list-style: none" >
                <strong>1. 2. et 3.</strong> l'utilisateur quitte la session
              </ul>
              <ul>
                retour à la homepage
              </ul>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <strong>Fin et Post-Conditions</strong>
            </td>
        </tr>
        <tr>
            <td>
                Fin
            </td>
            <td>
                <strong>L'utilisateur</strong> est redirigé vers une page de résultats
            </td>
        </tr>
        <tr>
            <td>
                Post-Conditions
            </td>
            <td>
                données des flèches enregistrées en base de données
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <strong>Compléments</strong>
            </td>
        </tr>
        <tr>
            <td>
                Ergonomie
            </td>
            <td>
                l'utilisateur doit cliquer sur une image l'endroit où est tombé la flèche
            </td>
        </tr>
        <tr>
            <td>
                Performances attendues
            </td>
            <td>
                RAS
            </td>
        </tr>
        <tr>
            <td>
                Problème non-résolu
            </td>
            <td>
                RAS
            </td>
        </tr>
    </tbody>
</table>