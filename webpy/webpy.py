# webpy.py

import reflex as rx

from .styles import styles
from .components.base import base_page
from . import routes
from .pages import profile_page, projects_page, contact_page


#animation test
wave: dict = {
    "@keyframes wave": {
        "0%": {"transform": "rotate(-15deg)"},
        "100%": {"transform": "rotate(45deg)"},
    }
}

# Index Page
def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.hstack(
                rx.heading("Bienvenid@!",size="8"),
                rx.heading(
                    "👋", size="7", 
                    style={
                        **wave,  # Spread the keyframes here
                        "animation": "wave 1s cubic-bezier(0.25,0.46,0.45,0.94) infinite alternate-reverse both"
                    },
                ),
                spacing="5",
            ),
            rx.text("Hola! En este espacio comparto información sobre mis proyectos. Bienvenid@!"),
            rx.text("(esta es una web estática)",size="1"),
            rx.vstack(
                rx.color_mode_cond(
                    light=rx.image(
                        src="img/inv_.png",
                        align="center",
                        width="250px",
                        height="auto",
                    ),
                    dark=rx.image(
                        src="img/logo_.png",
                        align="center",
                        width="250px",
                        height="auto",
                    ),
                ),
                rx.text(f"©2025 - maufranzar.com"),
                rx.text("Gracias por tu visita 🐸"),
                align_items="center",

                
            ),
            
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child",
        )
    return base_page(my_child)


app = rx.App(
    stylesheets=styles.STYLE_SHEETS,
    style=styles.BASE_STYLE
    )

app.add_page(
    index,
    title="maufranzar",
    description="porfolio maufranzar.com",
    image="/img/logo.ico"
)

app.add_page(
    profile_page,
    route=routes.urls.PROFILE,
    title="profile"
)

app.add_page(
    contact_page,
    route=routes.urls.CONTACT,
    title="profile"
)

app.add_page(
    projects_page,
    route=routes.urls.PROJECTS,
    title="profile"
)