import reflex as rx

from ..components.base import base_page
from .. import routes


def projects_page() -> rx.Component:
    child = rx.vstack(
            rx.heading("projects"),
            rx.text("This is the projects page."),
            rx.text("This is the projects page."),
            rx.text("This is the projects page."),
            rx.text("This is the projects page."),
            rx.text("This is the projects page."),
            rx.link(rx.button("Home",on_click=routes.urls.HOME)),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            )
    return base_page(child)          
    