## Package Authentification
### UC-4 - Supprimer son compte

<table>
    <tbody>
        <tr>
            <td>
                Acteurs Concernés
            </td>
            <td>
                Utilisateurs ayant un compte
            </td>
        </tr>
        <tr>
            <td>
                Description
            </td>
            <td>
                permet à un utilisateur de supprimer son compte
            </td>
        </tr>
        <tr>
            <td>
                Date
            </td>
            <td>
                12/05/2022
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
                <strong>L'utilisateur</strong> est connecté 
            </td>
        </tr>
        <tr>
            <td>
                Démarrage
            </td>
            <td>
                <strong>L'utilisateur</strong> est sur sa page de profil
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <strong>Dialogue</strong>
            </td>
        </tr>
        <tr>
            <td>
                Sénario nominal
            </td>
            <td>
              <ol>
                  <li>
                    <strong>L'utilisateur</strong> demande à supprimer son compte
                  </li>
                  <li>
                    <em>Le système</em> demande confirmation
                  </li>
                  <li>
                    <strong>L'utilisateur</strong> confirme
                  </li>
                  <li>
                    <em>Le système</em> supprime toutes les données de l'utilisateur puis le supprime et enfin le déconnecte
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
                  <li>
                        <strong>3.a</strong> l'utilisateur annule la suppression -> retour à la page de profil
                  </li>
                  <li>
                        <strong>Le système</strong> ne parvient pas à supprimer toutes les données de l'utilisateur
                        -> il devra ne pas supprimer le compte, et prévenir l'utilisateur qu'il y a un problème, qu'il faut contacter le service d'administration.
                  </li>
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
            <strong>L'utilisateur</strong> est sur la homepage
            </td>
        </tr>
        <tr>
            <td>
                Post-Conditions
            </td>
            <td>
                toutes les données de l'utilisateur sont supprimées, et il est déconnecté
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
                RAS
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