## Package Practice
### UC-4 - supprimer une session d'entrainement

<table>
    <tbody>
        <tr>
            <td>
                Acteurs Concernés
            </td>
            <td>
                utilisateur connecté
            </td>
        </tr>
        <tr>
            <td>
                Description
            </td>
            <td>
                permet à un utilisateur connecté de saisir les résultats lors d'une session d'entrainement
            </td>
        </tr>
        <tr>
            <td>
                Date
            </td>
            <td>
                24/05/2022
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
                utilisateur sur la page de détails d'un entrainement
            </td>
        </tr>
        <tr>
            <td>
                Démarrage
            </td>
            <td>
                l'utilisateur demande à ajouter les résultat d'une volée de flèches
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
                    <strong>L'utilisateur</strong> saisit la position de ses flèches et valide
                  </li>
                <li>
                    <em>le système</em> enregistre les scores de la volée, et en prépare une nouvelle
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
            </td>
        </tr>
        <tr>
            <td>
                Post-Conditions
            </td>
            <td>
                entrainement modifié en base
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <strong>Compléments</strong>
            </td>
            <td>
            </td>
        </tr>
        <tr>
            <td>
                Ergonomie
            </td>
            <td>
                <ul>
                    <li>
                        l'utilisateur pointe l'endroit dans une image d'où est arrivée la flèche. est sauvegardé en base sa position (pour les stats) et son score (pour le tableau de résultats)
                    </li>
                </ul>
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