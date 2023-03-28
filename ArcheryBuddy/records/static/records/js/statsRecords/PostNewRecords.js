import { AddDeleteClickListener } from "./listeners.js"

import { SaveShotsListener } from "./listeners.js"
const submitButton = document.querySelector('#shots-save')

submitButton.addEventListener("click", (e) => SaveShotsListener(e))
