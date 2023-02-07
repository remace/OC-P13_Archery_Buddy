
const submitButton = document.querySelector('#shots-save')
const ShotsElements = document.querySelectorAll('#shots-to-save > div')

const StatsRecordSessionTitleElement = document.querySelector('#srs-title')
const srsID = parseInt(StatsRecordSessionTitleElement.innerText.split(' ')[0].slice(1))

const CSRF = document.querySelector('input[name=csrfmiddlewaretoken]').value


submitButton.addEventListener("click", (e) => SaveShots(e))

function getCookie(name) {
    let cookie = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return cookie ? cookie[2] : null;
}

function SaveShots(e) {
    e.preventDefault()
    const ShotsElements = document.querySelectorAll('#shots-to-save > div')
    for (ShotElement of ShotsElements) {
        let arrow_id = parseInt(ShotElement.innerText.split(" • ")[0])
        let pos_x = parseFloat(ShotElement.innerText.split(" • ")[1])
        let pos_y = parseFloat(ShotElement.innerText.split(" • ")[2])


        //TODO popup
        arrow_id = 6

        let data = {
            "srs_id": srsID,
            "arrow_id": arrow_id,
            "pos_x": pos_x,
            "pos_y": pos_y,
        }

        options = {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data),
        }

        let res = fetch('/stats/record/create/', options)
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                return data
            })

        if (res == 200) {
            // ShotElement.delete()
            console.log(ShotElement)
            ShotElement.remove()
        }
    }
}