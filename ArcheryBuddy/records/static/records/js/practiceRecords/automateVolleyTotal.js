const fields = document.querySelectorAll(".text-field")
const totalFields = document.querySelectorAll('[id^="volley-total-"]')
const totalField = document.querySelector('#total')

fields.forEach((field) => {
    field.addEventListener('change', () => {
        /* demander de sélectionner une flèche dans la popup.
         si annulée, annuler la saisie de score*/
        update_color(field)
        updateVolleyTotal(field)
        updateTotal()
    })
    field.dispatchEvent(new Event('change'))
})


function updateVolleyTotal(field) {
    // get all the fields from the line and the total
    volley = field.id.split("-")[2] // input-score-{volley}-{shot}
    const volleyTotalField = document.querySelector(`#volley-total-${volley}`)
    const sameVolleyFieldsSelector = `[id^="input-score-${volley}"]`
    const sameVolleyFields = document.querySelectorAll(sameVolleyFieldsSelector)

    // calculate the total
    let total = 0
    sameVolleyFields.forEach((field) => {
        let value = parseInt(field.value)
        total += (isNaN(value) ? 0 : value)
    })
    volleyTotalField.innerHTML = total
}

function updateTotal() {
    let total = 0
    totalFields.forEach((field) => {
        let value = parseInt(field.innerHTML)
        total += (isNaN(value) ? 0 : value)
    })

    totalField.innerHTML = `total de l'entrainement: ${total}`
}

function update_color(field) {
    const YELLOW_ZONE_COLORS = ['rgb(255, 255, 0)', 'rgb(0, 0, 0)']
    const RED_ZONE_COLORS = ['rgb(255, 0, 0)', 'rgb(0, 0, 0)']
    const BLUE_ZONE_COLORS = ['rgb(51, 167, 255)', 'rgb(0, 0, 0)']
    const BLACK_ZONE_COLORS = ['rgb(0, 0, 0)', 'rgb(255, 255, 255)']
    const WHITE_ZONE_COLORS = ['rgb(255, 255, 255)', 'rgb(0, 0, 0)']

    score = parseInt(field.value)

    switch (score) {
        case 10:
        case 9:
            field.style.background = YELLOW_ZONE_COLORS[0]
            field.style.color = YELLOW_ZONE_COLORS[1]
            break;
        case 8:
        case 7:
            field.style.background = RED_ZONE_COLORS[0]
            field.style.color = RED_ZONE_COLORS[1]
            break;
        case 6:
        case 5:
            field.style.background = BLUE_ZONE_COLORS[0]
            field.style.color = BLUE_ZONE_COLORS[1]
            break;
        case 4:
        case 3:
            field.style.background = BLACK_ZONE_COLORS[0]
            field.style.color = BLACK_ZONE_COLORS[1]
            break;
        default:
            field.style.background = WHITE_ZONE_COLORS[0]
            field.style.color = WHITE_ZONE_COLORS[1]
            break;
    }

}
