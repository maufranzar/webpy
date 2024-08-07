import reflex as rx

from .navbar import navbar

def base_layout_componen(child, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            padding="1em",
            width="100%",
            id="content_area"
        ),
        rx.logo(),
    )
    
def base_page(child:rx.Component, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx. Component):
        child = rx.heading("Error: Invalid Child", size="1")
    return rx.fragment(
        base_layout_componen(child, *args, **kwargs),
    )