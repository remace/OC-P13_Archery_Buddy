const TARGET = document.querySelector("#target")
const SHOTSLIST = document.querySelector("#shots-to-save")

let DIALOG = document.querySelector("dialog")
let DIALOG_SUBMIT = document.querySelector("#modal-arrow-submit")
let DIALOG_CANCEL = document.querySelector("#modal-arrow-cancel")
let DIALOG_SELECT = document.querySelector(".arrow-modal-container form select")

let recordCanceled = true
let arrow_id = 0

let x;
let y;


TARGET.addEventListener('click', function onOpen(e) {
    x = e.offsetX
    y = e.offsetY

    DIALOG.showModal()
})

DIALOG_SELECT.addEventListener('change', function onSelect() {
    DIALOG_SUBMIT.value = DIALOG_SELECT.value
})


DIALOG_SUBMIT.addEventListener('click', function onClickSubmit(e) {
    arrow_id = e.target.value
    if (e.target.value != 'default') {
        addPoint(x, y)
        addRecordToList(x, y, arrow_id)
    }
    DIALOG.close()
})

DIALOG_CANCEL.addEventListener('click', function onClickCancel() {
    DIALOG.close()
})

function addPoint(x, y) {
    let newDiv = document.createElement('div')
    newDiv.classList.add("z-20")
    newDiv.classList.add("w-2")
    newDiv.classList.add("h-2")
    newDiv.classList.add("absolute")
    newDiv.classList.add(`left-[${x}px]`)
    newDiv.classList.add(`top-[${y}px]`)
    newDiv.classList.add(`bg-black`)
    newDiv.classList.add(`rounded-full`)
    newDiv.style.top = `${y}px`
    newDiv.style.left = `${x}px`
    TARGET.appendChild(newDiv)
}

function addRecordToList(x, y, arrow_id) {
    text = `${arrow_id} • ${x} • ${y} `


    newDiv = document.createElement('div')
    newDiv.classList.add("shot-to-save")
    content = document.createTextNode(text)

    newDiv.appendChild(content)

    newButton = document.createElement('button')
    newButton.innerText = "supprimer"
    newButton.classList.add("delete-unsaved")
    newButton.classList.add("cursor-pointer")
    newButton.classList.add("bg-red-500")
    newButton.classList.add("hover:bg-red-700")
    newButton.classList.add("font-bold")
    newButton.classList.add("py-2")
    newButton.classList.add("px-4")
    newButton.classList.add("rounded")
    newDiv.appendChild(newButton)

    SHOTSLIST.appendChild(newDiv)
}