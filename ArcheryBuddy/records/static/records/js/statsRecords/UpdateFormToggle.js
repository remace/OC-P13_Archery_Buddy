const TOGGLE_BUTTON = document.querySelector("#toggle-modify")
const FORM = document.querySelector("#modify-form")

TOGGLE_BUTTON.addEventListener("click", (e) => {
    FORM.classList.toggle("hidden")
})