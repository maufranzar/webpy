"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .components.base import base_page

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.text("child")
    )


app = rx.App()
app.add_page(index)

app.ad_page()
