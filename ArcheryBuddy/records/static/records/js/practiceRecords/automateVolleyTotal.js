const fields = document.querySelectorAll(".text-field")
const totalFields = document.querySelectorAll('[id^="volley-total-"]')
const totalField = document.querySelector('#total')

fields.forEach((field) => {
    field.addEventListener('change', () => {
        updateVolleyTotal(field)
        updateTotal()
    })
})


function updateVolleyTotal(field) {
    // get all the fields from the line and the total
    volley = field.id.split("-")[0]
    const volleyTotalField = document.querySelector(`#volley-total-${volley}`)
    const sameVolleyFieldsSelector = `[id^="${volley}"]`
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
