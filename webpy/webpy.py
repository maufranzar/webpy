"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .components.base import base_page
from . import routes
from .pages import (
    profile_page,
    projects_page,
    contact_page,
)


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.text("child")
    )


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
    title="Perfil",
)

app.add_page(
    projects_page,
    route=routes.urls.PROJECTS,
    title="Proyectos",
)

app.add_page(
    contact_page,
    route=routes.urls.CONTACT,
    title="Contacto",
)