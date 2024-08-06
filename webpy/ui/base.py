import reflex as rx

from . navbar import navbar


def base_page(child:rx.Component , hide_navbar=False,*args, **kwargs) -> rx.Component:
    # print([type(x) for x in args])
    if not isinstance(child, rx. Component):
        child = rx.heading("ERROR!!!!", size="5")
    if hide_navbar:
        return rx.container(
            child,
            rx.logo(),
            rx.color_mode.button(position="bottom-left"),
        )
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            padding="1em",
            width="100%",
            id="my-content-area",
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
        padding="10em",
        id="my-base-container",
    )