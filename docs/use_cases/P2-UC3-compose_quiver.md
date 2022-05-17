## Package Quiver
### UC-3 - composer un carquois

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
                permet à l'utilisateur d'optimiser ses choix de flèches
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
                page de résultat des flèches, L'utilisateur a déjà enregistré ses flèches
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
                      <strong>L'utilisateur</strong> demande le calcul de son carquois optimal. il saisit notamment le nombre de flèches d'une volée normale et nombre de flèches de rechange. (3+1,6+1, 6+2...)
                  </li>
                  <li>
                  <em>Le système</em> calcule le carquois optimal et lui affiche le résultat
                  </li>                  
              </ol>
            </td>
        </tr>
        <tr>
            <td>
                Scénario alternatif
            </td>
            <td>
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
                <strong>L'utilisateur</strong> est sur sa page de résultats
            </td>
        </tr>
        <tr>
            <td>
                Post-Conditions
            </td>
            <td>
                carquois optimal enregistré en base de données
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
                asynchrone? 
            </td>
        </tr>
        <tr>
            <td>
                Performances attendues
            </td>
            <td>
                moins de 5s de calcul pour un carquois d'une vingtaine de flèches
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