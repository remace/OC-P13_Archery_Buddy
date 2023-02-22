const TARGET = document.querySelector("#target")
const SHOTSLIST = document.querySelector("#shots-to-save")

let DIALOG = document.querySelector("#arrow-modal")
let DIALOG_SUBMIT = document.querySelector("#modal-arrow-submit")
let DIALOG_CANCEL = document.querySelector("#modal-arrow-cancel")
let DIALOG_SELECT = document.querySelector("#arrow-modal select")

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

DIALOG.addEventListener('close', function onClose() {
    if (DIALOG.returnValue !== "default") {
        // addPoint(x, y)
        console.log(DIALOG.returnValue)
        // addRecordToList(x, y, DIALOG.returnValue)
    }
})




function addPoint(x, y) {
    let newDiv = document.createElement('div')
    newDiv.classList.add("z-10")
    newDiv.classList.add("w-2")
    newDiv.classList.add("h-2")
    newDiv.classList.add("absolute")
    newDiv.classList.add(`left-[${x}px]`)
    newDiv.classList.add(`top-[${y}px]`)
    newDiv.classList.add(`bg-green`)
    newDiv.classList.add(`rounded-full`)
    newDiv.style.top = `${y}px`
    newDiv.style.left = `${x}px`
    TARGET.appendChild(newDiv)
}

function addRecordToList(x, y, arrow_id) {
    text = `${arrow_id} • ${x} • ${y}`

    newDiv = document.createElement('div')
    content = document.createTextNode(text)

    newDiv.appendChild(content)

    SHOTSLIST.appendChild(newDiv)
}