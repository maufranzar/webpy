import reflex as rx

from .. import routes
from .. styles import styles

def navbar_link(text:str, url:str) -> rx.Component:
    return rx.link(
        rx.text(text),
        href=url,
        size="5",
        underline="none",
        weight="medium"
    )
    
def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.color_mode.button(
                        size="3",
                        variant="outline",
                        radius="full",
                        high_contrast=True,
                        color=rx.color_mode_cond(light="dark", dark="light"),
                        background_color=rx.color_mode_cond(light="light", dark="dark"),
                        
                    ),
                    rx.box(
                        rx.link(
                            rx.text("mau", as_="span",size="8",weight="bold",style=styles.logo_style),
                            rx.text("fran", as_="span",size="8",weight="bold",style=styles.logo_style),
                            rx.text("zar", as_="span",size="8",weight="bold",style=styles.logo_style),
                            href=routes.urls.HOME,
                            underline="none",
                        ),
                    ),
                    spacing="5",
                ),
                rx.spacer(),
                rx.flex(
                    rx.hstack(
                        navbar_link("Home", routes.urls.HOME),
                        navbar_link("Profile", routes.urls.PROFILE),
                        navbar_link("Projects", routes.urls.PROJECTS),
                        navbar_link("Contact", routes.urls.CONTACT),
                        spacing="9"
                    ),
                ),
                rx.spacer(),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "🔒",
                            size="4",
                            variant="outline",
                            disabled=True,
                        ),
                    ),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            )
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.color_mode.button(
                        size="2",
                        variant="outline",
                        radius="full",
                        high_contrast=True,
                        color=rx.color_mode_cond(light="dark", dark="light"),
                        background_color=rx.color_mode_cond(light="light", dark="dark"),
                    ),
                    rx.box(
                        rx.link(
                            rx.text("mau", as_="span",size="7",weight="bold",style=styles.logo_style),
                            rx.text("fran", as_="span",size="7",weight="bold",style=styles.logo_style),
                            rx.text("zar", as_="span",size="7",weight="bold",style=styles.logo_style),
                            href=routes.urls.HOME,
                        ),
                    ),
                    spacing="4",
                ),
                rx.spacer(),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home",on_click=routes.state.NavState.to_home),
                        rx.menu.item("Profile",on_click=routes.state.NavState.to_profile),
                        rx.menu.item("Projects",on_click=routes.state.NavState.to_projects),
                        rx.menu.item("Contact",on_click=routes.state.NavState.to_contact),
                        rx.separator(),
                        rx.menu.item("Boton",on_click=routes.state.NavState.to_profile),
                        size="2",
                        align="center"
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),    
        ),
        bg=rx.color("accent",3),
        padding="0.8em",
        position="sticky",
        width="100%",
        id="navbar",
    )