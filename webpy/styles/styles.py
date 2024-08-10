import reflex as rx


CONTENT = "Poppins"
TITLE = "Comfortaa"
LOGO = "BioRhyme"


STYLE_SHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://fonts.googleapis.com/css2?family=BioRhyme:wght@200..800&display=swap"
    "/fonts/myfonts.css"
]

BASE_STYLE = {
    "font-family": CONTENT,
    rx.heading: {
        "font-family": TITLE,
    },
}

logo_style: dict = {
    "font-family" : LOGO}