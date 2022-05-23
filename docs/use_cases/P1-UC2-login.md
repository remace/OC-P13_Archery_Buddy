## Package Authentification
### UC-2 - se connecter à son compte

<table>
    <tbody>
        <tr>
            <td>
                Acteurs Concernés
            </td>
            <td>
                tout Utilisateur
            </td>
        </tr>
        <tr>
            <td>
                Description
            </td>
            <td>
                permet à un utilisateur non-connecté de se connecter
            </td>
        </tr>
        <tr>
            <td>
                Date
            </td>
            <td>
                11/05/2022
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
                Utilisateur non-connecté
            </td>
        </tr>
        <tr>
            <td>
                Démarrage
            </td>
            <td>
                <strong>l'utilisateur<strong> sur trouve sur la homepage
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
                    <strong>L'utilisateur</strong> demande à se connecter à son compte
                  </li>
                  <li>
                    <em>Le système</em> sert un formulaire pour lui demander identifiant et mot de passe
                  </li>
                  <li>
                    <strong>L'utilisateur</strong> entre les données nécessaires
                  </li>
                  <li>
                    <em>le système</em> vérifie ses identifiant, et le renvoie vers la homepage
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
                      <strong>4.a</strong> l'utilisateur a donné de mauvais identifiants -> le système redirige sur le formulaire de l'étape 2, avec une popup expliquant que les identifiants sont peut-être erronés
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
              <strong>L'utilisateur</strong>, si existant, est connecté
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