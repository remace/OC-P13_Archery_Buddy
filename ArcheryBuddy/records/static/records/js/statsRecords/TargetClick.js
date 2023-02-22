const TARGET = document.querySelector("#target")
const SHOTSLIST = document.querySelector("#shots-to-save")

const MODAL = document.querySelector("#arrow-modal")
const MODAL_SUBMIT = document.querySelector("#modal-arrow-submit")
const MODAL_CANCEL = document.querySelector('#modal-arrow-cancel')

console.log(MODAL) // should return a div, returns null
console.log(MODAL_SUBMIT) // should return a div returns null
console.log(MODAL_CANCEL) // should return a div returns null

let recordCanceled = true
let arrow_id = 0


TARGET.addEventListener('click', (e) => {
    let x = e.offsetX
    let y = e.offsetY

    console.log("target event")

    //modal
    MODAL.classList.toggle("hidden")
    MODAL_SUBMIT.addEventListener('click', function modal_submit(e) {
        arrow_id = 6 ///numero à extraire
        MODAL.classList.toggle("hidden")
        recordCanceled = false

        MODAL_SUBMIT.removeEventListener('click', modal_submit())

    })

    MODAL_SUBMIT.addEventListener('click', function modal_cancel(e) {
        MODAL.classList.toggle("hidden")
        recordCanceled = true
    })


    if (recordCanceled !== false) {
        return
    }
    add_point(x, y)
    addRecordToList(x, y, arrow_id)
})

MODAL_SUBMIT.addEventListener('click', (e) => {
    arrow_id = 6 ///numero à extraire
    MODAL.classList.toggle("hidden")
    recordCanceled = false
})

MODAL_SUBMIT.addEventListener('click', (e) => {
    MODAL.classList.toggle("hidden")
    recordCanceled = true
})

function add_point(x, y) {
    let newDiv = document.createElement('div')
    newDiv.classList.add("z-10")
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
    text = `${arrow_id} • ${x} • ${y}`

    newDiv = document.createElement('div')
    content = document.createTextNode(text)

    newDiv.appendChild(content)

    SHOTSLIST.appendChild(newDiv)
}