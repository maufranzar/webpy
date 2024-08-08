import reflex as rx

from ..components.base import base_page
from .. import routes

import reflex as rx

    
def link_icon(image:str, url:str) -> rx.Component:
    return rx.link(
        rx.icon(
            image,
            size=30,
        ),
        href=url,
        is_external=True
    )
    
       
def profile_content() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/img/me_bg.png",
                fallback="MFS",
                variant="soft",
                radius="full",
                size="7",
            ),
            rx.vstack(
                rx.heading("Mauricio Franco Salazar", size="6"),
                rx.badge(
                    rx.icon("fingerprint", size=15),
                    rx.text("maufranzar", size="2"),
                    spacing="1"    
                ),
                rx.hstack(
                    rx.flex(
                        link_icon(
                            "github",
                            routes.urls.GITHUB,
                        ),
                        link_icon(
                            "linkedin",
                            routes.urls.LINKEDIN,
                        ),
                        link_icon(
                            "twitter",
                            routes.urls.TWITTER,
                        ),
                        link_icon(
                            "headphones",
                            routes.urls.SPOTIFY,
                        ),
                        spacing="7",
                    )
                )
            ),
            spacing="6",
        ),
        rx.divider(
            height="2px",
            border_radius="2px"
        ),
        spacing="4",
    )
    
def profile_description() -> rx.Component:
    return rx.container(
        rx.accordion.root(
            rx.accordion.item(
                header=rx.heading("Perfil", size="4"),
                content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            ),
            rx.accordion.item(
                header=rx.heading("Formación", size="4"),
                content=rx.card(
                    rx.list(
                        rx.list.item(
                        rx.icon("school",size=20,align="center"),
                        "Universidad Ricardo Palma: Ingeniería Electrónica"
                        ),
                        rx.list.item(
                        rx.icon("school",size=20,align="center"),
                        "Universidad Ricardo Palma: Ingeniería Electrónica"
                        ),
                        rx.list.item(
                        rx.icon("school",size=20,align="center"),
                        "Universidad Ricardo Palma: Ingeniería Electrónica"
                        )
                    )
                ),
                justify="vertical",
            ),
            rx.accordion.item(
                header=rx.heading("Experiencia", size="4"),
                content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            ),
            collapse=True,
            orientation="vertical",
            width="100%",
            variant="outline",
            radius="medium",
        )
    )

@rx.page(route=routes.urls.PROFILE)
def profile_page() -> rx.Component:

    my_child = rx.container(
        rx.vstack(
        profile_content(),
        profile_description(),
        spacing="5",
        #justify="center",
        align="center",
        min_height="85vh",
        id="my-child",
        )
    )
    return base_page(my_child)      
    