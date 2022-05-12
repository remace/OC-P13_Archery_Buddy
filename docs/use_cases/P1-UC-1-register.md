## Package Authentification
### UC-1 - créer un compte

<table>
    <tbody>
        <tr>
            <td>
                Acteurs Concernés
            </td>
            <td>
                Tout Utilisateur
            </td>
        </tr>
        <tr>
            <td>
                Description
            </td>
            <td>
                permet à n'importe quel user de se créer un compte
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
                auteur
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
                Aucune
            </td>
        </tr>
        <tr>
            <td>
                Démarrage
            </td>
            <td>
                <strong>l'utilisateur</strong> est non-connecté, sur la homepage
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
                    <strong>l'utilisateur</strong> clique sur un bouton "sign up" in dans la barre de titre
                  </li>
                  <li>
                    <em>le système</em> lui sert un formulaire
                  </li>
                  <li>
                    <strong>l'utilisateur</strong> le remplit et le soumet
                  </li>
                  <li>
                    <em>le système</em> crée le compte selon les données soumises.
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
                      <strong>4.a</strong> les données du formulaire ne respectent pas les standards (identifiant déjà utilisé, mot de passe trop court, ou mot de passe confirmé différent): le système l'indique à l'utilisateur grâce à un petit encart rouge, et reste sur le formulaire
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
                <strong>l'utilisateur</strong> est redirigé vers la home page
            </td>
        </tr>
        <tr>
            <td>
                Post-Conditions
            </td>
            <td>
                utilisateur créé en base de données.
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
                ne pas attendre que le formulaire soit posté pour en afficher les contraintes non-respectées sur le mot de passe
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