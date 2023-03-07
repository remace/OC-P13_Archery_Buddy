
const submitButton = document.querySelector('#shots-save')
const ShotsElements = document.querySelectorAll('#shots-to-save > div')
const SavedShotsElement = document.querySelector('.saved-shots-container')

const StatsRecordSessionTitleElement = document.querySelector('#srs-title')
const srsID = parseInt(StatsRecordSessionTitleElement.innerText.split(' ')[0].slice(1))

const CSRF = document.querySelector('input[name=csrfmiddlewaretoken]').value


submitButton.addEventListener("click", (e) => SaveShots(e))

function getCookie(name) {
    let cookie = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return cookie ? cookie[2] : null;
}

async function SaveShots(e) {
    e.preventDefault()
    const ShotsElements = document.querySelectorAll('.shot-to-save')

    for (ShotElement of ShotsElements) {
        let arrow_id = parseInt(ShotElement.innerText.split(" • ")[0])
        let pos_x = parseFloat(ShotElement.innerText.split(" • ")[1])
        let pos_y = parseFloat(ShotElement.innerText.split(" • ")[2])


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

        let result = await fetch('/stats/record/create/', options)
            .then(function (response) {
                return response.status
            })

        if (result == 200) {
            let newP = document.createElement("p")
            newP.classList.add(`flagged-p`)
            newP.innerText = `${arrow_id} • ${pos_x} • ${pos_y}`
            SavedShotsElement.appendChild(newP)
            ShotElement.parentNode.removeChild(ShotElement)
        } else {
            console.log("erreur pendant la création de l'enregistrement")
        }
    }
}