import reflex as rx

from .components.base import base_page
from . import routes
from .pages import profile_page, projects_page, contact_page

# Index Page

def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.link(
                rx.button("PROFILE"),
            ),
            rx.link(
                rx.button("contact"),
            ),
            spacing="5",
            justify="center",
            align="center",
            text_align="center",
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