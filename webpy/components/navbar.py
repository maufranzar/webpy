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
                            rx.text("mau", as_="span",size="7"),
                            rx.text("fran", as_="span",size="7"),
                            rx.text("zar", as_="span",size="7"),
                            href=routes.urls.HOME,
                        ),
                    ),
                    spacing="4",
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
                            "boton",
                            size="3",
                            variant="outline",
                        ),
                        href=routes.urls.PROFILE,
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
                            rx.text("mau", as_="span",size="7"),
                            rx.text("fran", as_="span",size="7"),
                            rx.text("zar", as_="span",size="7"),
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
                        rx.menu.item("Home", on_click=routes.state.NavState.to_home),
                        rx.menu.item("Profile", on_click=routes.state.NavState.to_profile),
                        rx.menu.item("Projects", on_click=routes.state.NavState.to_projects),
                        rx.menu.item("Contact", on_click=routes.state.NavState.to_contact),
                        rx.separator(),
                        rx.menu.item("Boton", on_click=routes.state.NavState.to_profile),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),    
        ),
        bg=rx.color("accent",3),
        padding="1em",
        position="sticky",
        # top="0px",
        # z_index="5",
        width="100%",
        id="navbar",
    )