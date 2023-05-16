export function getCookie(name) {
    let cookie = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return cookie ? cookie[2] : null;
}

export function AddDeleteClickListener(button) {
    button.addEventListener('click', async function (e) {
        e.preventDefault()
        e.target.toggleAttribute("disabled", false)
        let record_id = e.target.parentElement.parentElement.children[0].innerText
        const URI = `/stats/103/record/${record_id}/delete/`

        let options = {
            method: "GET",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            }
        }

        let result = await fetch(URI, options = options)
            .then(function (response) {
                return response.json()
            })


        if (result.status_code == 200) {

            let arrow_id = result.data.arrow_id
            let pos_x = result.data.pos_x
            let pos_y = result.data.pos_y

            e.target.parentElement.parentElement.parentElement.removeChild(e.target.parentElement.parentElement)
            let dot_on_target = document.getElementById(`shot-dot-${arrow_id}-${pos_x}-${pos_y}`)
            dot_on_target.parentElement.removeChild(dot_on_target)
        } else {
            console.log("erreur pendant la suppression côté serveur")
        }
    })
}

export async function SaveShotsListener(e) {

    e.preventDefault()

    const SavedShotsElement = document.querySelector('.saved-shots-container')
    const StatsRecordSessionTitleElement = document.querySelector('#srs-title')
    const srsID = parseInt(StatsRecordSessionTitleElement.innerText.split(' ')[0].slice(1))
    const CSRF = document.querySelector('input[name=csrfmiddlewaretoken]').value

    const ShotsElements = document.querySelectorAll('.shot-to-save')

    for (let ShotElement of ShotsElements) {
        let arrow_id = parseInt(ShotElement.children[0].innerText)
        let pos_x = parseFloat(ShotElement.children[1].innerText)
        let pos_y = parseFloat(ShotElement.children[2].innerText)


        const data = new FormData()
        data.append("srs_id", srsID)
        data.append('arrow_id', arrow_id)
        data.append('pos_x', pos_x)
        data.append('pos_y', pos_y)

        let options = {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: data,
        }

        let response = await fetch('/stats/record/create/', options)
            .then(function (response) {
                return response.json()
            })

        let responseData = JSON.parse(response)

        if (responseData.status_code == 200) {

            let newTr = document.createElement("tr")

            let shot_id = responseData.record.id

            let newDeleteButton = document.createElement("button")
            newDeleteButton.innerText = "supprimer"
            newDeleteButton.classList.add("delete-saved")
            newDeleteButton.classList.add("cursor-pointer")
            newDeleteButton.classList.add("bg-red-500")
            newDeleteButton.classList.add("hover:bg-red-700")
            newDeleteButton.classList.add("font-bold")
            newDeleteButton.classList.add("py-2")
            newDeleteButton.classList.add("px-4")
            newDeleteButton.classList.add("rounded")

            AddDeleteClickListener(newDeleteButton)

            let tdShotid = document.createElement('th')
            tdShotid.classList.add("px-6")
            tdShotid.classList.add("item-center")
            tdShotid.classList.add("py-2")
            tdShotid.setAttribute("scope", "row")
            let content = document.createTextNode(shot_id)
            tdShotid.appendChild(content)

            let tdArrowid = document.createElement('td')
            tdArrowid.classList.add("px-6")
            tdArrowid.classList.add("text-center")
            tdArrowid.classList.add("py-2")
            content = document.createTextNode(arrow_id)
            tdArrowid.appendChild(content)

            let tdPosX = document.createElement('td')
            tdPosX.classList.add("px-6")
            tdPosX.classList.add("text-center")
            tdPosX.classList.add("py-2")
            content = document.createTextNode(pos_x.toFixed(1).replace('.', ','))
            tdPosX.appendChild(content)

            let tdPosY = document.createElement('td')
            tdPosY.classList.add("px-6")
            tdPosY.classList.add("text-center")
            tdPosY.classList.add("py-2")
            content = document.createTextNode(pos_y.toFixed(1).replace('.', ','))
            tdPosY.appendChild(content)

            let tdDeleteButton = document.createElement('td')
            tdDeleteButton.classList.add("px-6")
            tdDeleteButton.classList.add("py-2")
            tdDeleteButton.appendChild(newDeleteButton)

            newTr.appendChild(tdShotid)
            newTr.appendChild(tdArrowid)
            newTr.appendChild(tdPosX)
            newTr.appendChild(tdPosY)
            newTr.appendChild(tdDeleteButton)

            SavedShotsElement.appendChild(newTr)

            ShotElement.parentNode.removeChild(ShotElement)
        } else {
            console.log("erreur pendant la création de l'enregistrement")
        }
    }
}