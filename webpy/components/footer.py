import reflex as rx





def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            rxc="/img/logo_.png",
            width="100px",
            height="auto",
        ),
        rx.text("Gracias por tu visita"),
        rx.logo(),
    )