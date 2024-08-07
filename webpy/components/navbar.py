import reflex as rx

from .. import routes

def navbar_link(text:str, url:str) -> rx.Component:
    return rx.link(
        rx.text(text),
        href=url,
    )
    
def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.button(
                        
                    ),
                    rx.box(
                        rx.link(
                            rx.text("mau", as_="span"),
                            rx.text("fran", as_="span"),
                            rx.text("zar", as_="span"),
                            href=routes.urls.HOME,
                        ),
                    )
                ),
                rx.spacer(),
                rx.flex(
                    rx.hstack(
                        navbar_link("Home", routes.urls.HOME),
                        navbar_link("Profile", routes.urls.PROFILE),
                        navbar_link("Contact", routes.urls.CONTACT),
                        spacing="5"
                    ),
                )

            )
        ),
        rx.mobile_and_tablet(
            rx.heading("Reflex", size="3"),
        ),
        bg=rx.color("accent",3),
        padding="1em",
        position="sticky",
        # top="0px",
        # z_index="5",
        width="100%",
        id="navbar",
    )