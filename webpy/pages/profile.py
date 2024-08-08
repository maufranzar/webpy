import reflex as rx

from ..components.base import base_page
from .. import routes

import reflex as rx

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.text(title,as_="span"),
        f" {body}",
        align="center",
        justify="center",
    )
    

def link_icon(image:str, url:str) -> rx.Component:
    return rx.link(
        rx.icon(
            image,
            size=30,
        ),
        href=url,
        is_external=True
    )
    
    
    
def link_button(title:str, image:str ,body:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width="50px",
                    height="50px",
                    margin="5px",
                    alt = title
                ),
                rx.vstack(
                    rx.heading(title),
                    rx.text(body),
                    align_items="start",
                    justify="center",
                ),
                width="100%",
            ),
            # 
        ),
        href=url,
        is_external=True,
        width="100%"
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
                rx.heading("Mauricio Franco", size="6"),
                rx.text("@maufranzar"),
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
            )
        )
    )
    



@rx.page(route=routes.urls.PROFILE)
def profile_page() -> rx.Component:

    my_child = rx.vstack(
        profile_content(),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id="my-child",
        )
    return base_page(my_child)      
    