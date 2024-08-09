import reflex as rx

from .navbar import navbar


def base_layout_componen(child, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            aling_items="center",
            padding="1em",
            width="100%",
            id="content_area",
            z_index="999"
        ),
        rx.logo(),
    )
    
def base_page(child:rx.Component, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx. Component):
        child = rx.heading("Error: Invalid Child", size="7")
    return rx.fragment(
        base_layout_componen(child, *args, **kwargs),
    )