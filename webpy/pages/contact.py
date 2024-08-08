import reflex as rx
from .. components.base import base_page
from .. import routes

    

def form_field(
    label: str, placeholder: str, type: str, name: str
) -> rx.Component:
    return rx.form.field(
        rx.flex(
            rx.form.label(label),
            rx.form.control(
                rx.input(
                    placeholder=placeholder,
                    type=type,
                    required=True
                ),
                as_child=True,
            ),
            direction="column",
            spacing="1",
        ),
        name=name,
        width="100%",
        )
    

    
def contact_form() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="mail-plus", size=40),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.heading(
                        "Envia un mensaje a",
                        size="5",
                        weight="bold",
                    ),
                    rx.text(
                        "📨 contact@maufranzar.com",
                        size="3",
                    ),
                    spacing="2",
                    height="100%",
                ),
                height="100%",
                spacing="4",
                align_items="center",
                width="100%",
            ),
            rx.form.root(
                rx.flex(
                    rx.flex(
                        form_field(
                            "Nombre",
                            "Mauricio",
                            "text",
                            "first_name",
                        ),
                        form_field(
                            "Apellido",
                            "Franco Salazar",
                            "text",
                            "last_name",
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        form_field(
                            "Email",
                            "tu@correo.com",
                            "email",
                            "email",
                        ),
                        form_field(
                            "Celular",
                            "Celular",
                            "tel", 
                            "phone",
                        ),
                        spacing="3",
                        flex_direction=[
                            "column",
                            "row",
                            "row",
                        ],
                    ),
                    rx.flex(
                        rx.text(
                            "Mensaje",
                            style={
                                "font-size": "15px",
                                "font-weight": "500",
                                "line-height": "35px",
                            },
                        ),
                        rx.text_area(
                            placeholder="Escribe aqui tu mensaje",
                            name="message",
                            resize="vertical",
                            required=True,
                            limit=300,                          
                        ),
                        direction="column",
                        spacing="1",
                    ),
                    rx.form.submit(
                        rx.button("Enviar mensaje"),
                        as_child=True,
                    ),
                    direction="column",
                    spacing="2",
                    width="100%",
                ),
                on_submit=lambda form_data: rx.window_alert(
                    form_data.to_string(),
                ),
                reset_on_submit=False,
                
            ),
            width="100%",
            direction="column",
            spacing="4",
        ),
        size="3",
    )


@rx.page(route=routes.urls.CONTACT)
def contact_page() -> rx.Component:

    my_child = rx.vstack(
            contact_form(),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child",
        )
    return base_page(my_child)

