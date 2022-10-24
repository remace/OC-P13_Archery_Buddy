const SELECTOR = document.getElementById("bow_type_selector")
const BAREBOWFORM = document.getElementById("BarebowBowForm")
const OLYMPICBOWFORM = document.getElementById("OlympicBowForm")
const COMPOUNDBOWFORM = document.getElementById("CompoundBowForm")

const HIDDENSUBFORMSCONTAINER = document.getElementById("hiddenSubFormsContainer")
const SUBFORMCONTAINER = document.getElementById("subFormContainer")


function removeFormerBowTypeForm() {
    formToRemove = SUBFORMCONTAINER.children[0]
    HIDDENSUBFORMSCONTAINER.appendChild(formToRemove)
}

function addNewBowTypeForm(newBowType) {
    newFormId = newBowType + "BowForm"
    newForm = document.getElementById(newFormId)
    SUBFORMCONTAINER.appendChild(newForm)
}


SELECTOR.addEventListener('change', (e) => {
    newBowType = SELECTOR.options[SELECTOR.selectedIndex].value
    removeFormerBowTypeForm()
    addNewBowTypeForm(newBowType)
})