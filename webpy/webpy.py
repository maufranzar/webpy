import reflex as rx

from .components.base import base_page


# Index Page

def index() -> rx.Component:
    my_child = rx.center(
        rx.heading("Bienvenido a mi web personal", size="7"),
        spacing="9",
        justify_content="center",
        align_items="center",
        flex_wrap="wrap",
    )
    return base_page(my_child)


app = rx.App()

app.add_page(
    index,
    title="maufranzar",
    description="web personal de maufranzar",
    image="/img/logo.ico"
)
