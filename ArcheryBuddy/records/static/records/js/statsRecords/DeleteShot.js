const SAVED_SHOT_DELETE_LINKS = document.querySelectorAll(".delete-link")
const UNSAVED_SHOT_DELETE_LINKS = document.querySelectorAll(".btn-delete-unsaved")

SAVED_SHOT_DELETE_LINKS.forEach(function (link) {
    link.addEventListener('click', async function (e) {
        e.preventDefault()
        record_id = e.target.parentElement.innerText.split('•')[0].trim()
        const URI = `http://127.0.0.1:8000/stats/103/record/${record_id}/delete/`

        options = {
            method: "GET",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            }
        }

        let result = await fetch(URI, options = options)
            .then(function (response) {
                return response.status
            })

        if (result == 200) {
            e.target.parentElement.parentElement.removeChild(e.target.parentElement)
        } else {
            console.log("erreur pendant la suppression côté serveur")
        }

    })
})