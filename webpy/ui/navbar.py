import reflex as rx

from .. import navigation


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="5", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
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
                    rx.link(                
                        rx.heading(
                        "MAUFRANZAR", 
                        size="7", 
                        weight="bold",
                    ),
                    href=navigation.routes.HOME_ROUTE,
                    align_items="center",
                    ),
                    spacing="5",
                ),
                rx.hstack(
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("About", navigation.routes.ABOUT_ROUTE),
                    navbar_link("Contact", navigation.routes.CONTACT_ROUTE),
                    spacing="8",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
                id="my-navbar-hstack-desktop",        
            ),
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
                    rx.link(
                        rx.heading(
                            "MAUFRANZAR", 
                            size="6", 
                            weight="bold",
                        ),
                        href=navigation.routes.HOME_ROUTE,
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home",on_click=navigation.NavState.to_home_page),
                        rx.menu.item("About",on_click=navigation.NavState.to_about_page),
                        rx.menu.item("Contact",on_click=navigation.NavState.to_contact_page),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        id="my-navbar",
    )