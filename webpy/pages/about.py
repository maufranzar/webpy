import reflex as rx
from .. ui.base import base_page
from .. import navigation

def about_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("ABOUT",size="9"),
            rx.text(
                "ABOUT... ",
            ),
            rx.link(
                rx.button("home"),
                href=navigation.routes.HOME_ROUTE
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child",
        )
    return base_page(my_child)