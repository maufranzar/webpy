import reflex as rx

from .components.base import base_page
from . import routes
from .pages import profile_page, projects_page, contact_page

# Index Page
wave: dict = {
    "@keyframes wave": {
        "0%": {"transform": "rotate(-15deg)"},
        "100%": {"transform": "rotate(45deg)"},
    }
}

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

            rx.text("En este espacio comparto informacion sobre mis proyectos e intereses."),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child",
        )
    return base_page(my_child)


app = rx.App()

app.add_page(
    index,
    title="maufranzar",
    description="web personal de maufranzar",
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