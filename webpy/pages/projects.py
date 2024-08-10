import reflex as rx

from .. components.base import base_page
from .. import routes



@rx.page(route=routes.urls.PROJECTS)
def projects_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("PROYECTOS",size="9"),
            rx.text("En contruccion... ",),
            rx.heading(
                    "🐍"
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child",
        )
    return base_page(my_child)