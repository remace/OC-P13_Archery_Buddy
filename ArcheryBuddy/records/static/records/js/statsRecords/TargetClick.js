const TARGET = document.querySelector("#target")
const SHOTSLIST = document.querySelector("#shots-to-save-table-body")

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
        console.log(x, y, arrow_id)
        addPoint(x, y, arrow_id)
        addRecordToList(x, y, arrow_id)
    }
    DIALOG_SELECT.value = "default"
    DIALOG.close()
})

DIALOG_CANCEL.addEventListener('click', function onClickCancel() {
    DIALOG.close()
})

function addPoint(x, y, arrow_id) {
    let newDiv = document.createElement('div')
    newDiv.classList.add("z-20")
    newDiv.classList.add("w-1")
    newDiv.classList.add("h-1")
    newDiv.classList.add("absolute")
    newDiv.classList.add(`left-[${x}px]`)
    newDiv.classList.add(`top-[${y}px]`)
    newDiv.classList.add(`bg-green-500`)
    newDiv.classList.add(`rounded-full`)
    newDiv.style.top = `${y}px`
    newDiv.style.left = `${x}px`
    newDiv.id = `shot-dot-${arrow_id}-${x}-${y}`
    TARGET.appendChild(newDiv)
}

function addRecordToList(x, y, arrow_id) {
    let idTh = document.createElement('th')
    let content = document.createTextNode(arrow_id)
    idTh.appendChild(content)

    idTh.classList.add("px-6")
    idTh.classList.add("py-2")
    idTh.classList.add("text-center")

    let xTd = document.createElement('td')
    content = document.createTextNode(x)
    xTd.appendChild(content)

    xTd.classList.add("px-6")
    xTd.classList.add("py-2")
    xTd.classList.add("text-center")


    let yTd = document.createElement('td')
    content = document.createTextNode(y)
    yTd.appendChild(content)
    yTd.classList.add("px-6")
    yTd.classList.add("py-2")
    yTd.classList.add("text-center")

    let newTr = document.createElement('tr')
    newTr.classList.add("shot-to-save")
    newTr.appendChild(idTh)
    newTr.appendChild(xTd)
    newTr.appendChild(yTd)

    SHOTSLIST.appendChild(newTr)
}