let ARROWS = document.getElementsByClassName("arrow-container")


function getPointFromArrow(element) {

    let arrow_id = element.children[0].innerText
    let pos_x = Math.round(parseFloat(element.children[1].innerText.replace(',', '.'))).toString()
    let pos_y = Math.round(parseFloat(element.children[2].innerText.replace(',', '.'))).toString()
    let point = document.getElementById(`shot-dot-${arrow_id}-${pos_x}-${pos_y}`)
    return point
}


function HighlightArrow(event) {
    let dotElement = getPointFromArrow(event.target)
    dotElement.classList.add("bg-violet-700")
    dotElement.classList.remove("bg-green-500")
}
function UnHighlightArrow(event) {
    let dotElement = getPointFromArrow(event.target)
    dotElement.classList.add("bg-green-500");
    dotElement.classList.remove("bg-violet-700");
}

for (let arrow of ARROWS) {
    arrow.addEventListener("mouseenter", function (event) { HighlightArrow(event) })
    arrow.addEventListener("mouseleave", function (event) { UnHighlightArrow(event) })
}