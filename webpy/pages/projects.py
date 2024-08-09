import reflex as rx

from ..components.base import base_page
from .. import routes



def projects_content() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.heading(
                "Profile",
                size="4",
                weight="bold",
            ),
            rx.text(
                "Projects!!",
                size="2",
            ),
            spacing="1",
            height="100%",
        ),
        padding="2",
        width="100%",
        height="100%",
    )



@rx.page(route=routes.urls.PROJECTS)
def projects_page() -> rx.Component:

    my_child = rx.vstack(
        rx.heading("EN CONSTRUCCION!",size="7"),
        projects_content(),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id="my-child",
        )
    return base_page(my_child)      
    