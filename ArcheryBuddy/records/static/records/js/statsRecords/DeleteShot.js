import { AddDeleteClickListener } from "./listeners.js"

const SAVED_SHOT_DELETE_BUTTONS = document.querySelectorAll(".delete-saved")

SAVED_SHOT_DELETE_BUTTONS.forEach((button) => AddDeleteClickListener(button))