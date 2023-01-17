const TARGET = document.querySelector("#target")
const SHOTSLIST = document.querySelector("#shots-to-save")


TARGET.addEventListener('click', (e) => {
    x = e.offsetX
    y = e.offsetY

    //modal
    //TODO

    //ajouter un point
    add_point(x, y)

    addRecordToList(x, y, 6)
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