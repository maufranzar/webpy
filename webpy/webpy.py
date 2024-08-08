import reflex as rx

from .components.base import base_page
from . import routes, pages


# Index Page

def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.link(
                rx.button("Projects!!!"),
            ),
            rx.link(
                rx.button("contact"),
            ),
            spacing="5",
            justify="center",
            align="center",
            text_align="center",
            min_height="85vh",
        )
    return base_page(my_child)


app = rx.App()

app.add_page(
    index,
    title="maufranzar",
    description="web personal de maufranzar",
    image="/img/logo.ico"
)
