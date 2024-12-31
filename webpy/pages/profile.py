import reflex as rx
from ..components.base import base_page
from .. import routes


def link_icon(image: str, url: str) -> rx.Component:
    return rx.link(
        rx.icon(image, size=30),
        href=url,
        is_external=True
    )


def profile_content() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/img/me_bg.png",
                fallback="MFS",
                variant="soft",
                radius="full",
                size="8",
            ),
            rx.vstack(
                rx.heading("Mauricio Franco Salazar", size="6"),
                rx.badge(
                    rx.icon("fingerprint", size=15),
                    rx.text("maufranzar", size="2"),
                    spacing="1"
                ),
                rx.hstack(
                    rx.flex(
                        link_icon("github", routes.urls.GITHUB),
                        link_icon("linkedin", routes.urls.LINKEDIN),
                        link_icon("twitter", routes.urls.TWITTER),
                        link_icon("headphones", routes.urls.SPOTIFY),
                        spacing="7",
                    )
                )
            ),
            spacing="6",
        ),
        rx.divider(height="2px", border_radius="2px"),
        spacing="4",
    )


def profile_description() -> rx.Component:
    return rx.container(
        rx.accordion.root(
            # 1. PERFIL PROFESIONAL
            rx.accordion.item(
                header=rx.heading("Perfil Profesional", size="4"),
                content=rx.container(
                        rx.box(
                        rx.text(
                            "Soy Bachiller en Ingeniería Electrónica, me apasiona la tecnología y el poder que tiene para mejorar nuestras vidas. Sin embargo, el acceso a esta no es igual para todos. Me motiva poder contribuir a reducir tal brecha.",
                                style={"text-align": "justify"}
                            ),
                        ),
                        rx.box(
                            rx.text(
                                "Actualmente, me encuentro efocado en tecnologías emergentes como IoT, BigData e IA. Te invito a que puedas ver el proyecto que expongo aquí",
                                style={"text-align": "justify"}
                                ),
                            ),
                    justify="between",
                    spacing="4",
                      ),
            ),
            # 2. FORMACIÓN ACADÉMICA
            rx.accordion.item(
                header=rx.heading("Formación Académica", size="4"),
                content=rx.vstack(
                    rx.card(
                        rx.flex(
                            rx.box(
                                rx.heading("Universidad Ricardo Palma", size="5"),
                                rx.text("Ingeniería Electrónica", size="3"),
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        as_child=True,
                        width="100%",
                    ),
                    rx.card(
                        rx.flex(
                            rx.box(
                                rx.heading("Platzi", size="5"),
                                rx.text("Fundamentos de Servidores Linux", size="3"),
                                rx.text("Análisis y Manipulación de Datos con Python", size="3"),
                                rx.text("Machine Learning con Python", size="3"),
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        as_child=True,
                        width="100%",
                    ),
                    orientation="vertical",
                    spacing="4",
                ),
                width="100%",
                justify="vertical",
            ),
            
            # 4. CERTIFICACIONES
            rx.accordion.item(
                header=rx.heading("Certificaciones", size="4"),
                content=rx.vstack(
                    rx.card(
                        rx.flex(
                            rx.box(
                                rx.heading("Universidad Ricardo Palma", size="5"),
                                rx.unordered_list(
                                    rx.list_item(
                                        "Inglés Profesional Intermedio",
                                        style={"font-size": "14px"}
                                    ),
                                ),
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        as_child=True,
                        width="100%",
                    ),
                    rx.card(
                        rx.flex(
                            rx.box(
                                rx.heading("Platzi Links", size="5"),
                                rx.unordered_list(
                                    rx.list_item(
                                        rx.link(
                                            "Fundamentos de Servidores Linux",
                                            href=routes.urls.PLAT_LINUX,
                                            is_external=True,
                                        ),
                                        style={"font-size": "14px"},
                                    ),
                                    rx.list_item(
                                        rx.link(
                                            "Análisis, Manipulación y Visualización de Datos con Python",
                                            href=routes.urls.PLAT_DATOS,
                                            is_external=True,
                                        ),
                                        style={"font-size": "14px"},
                                    ),
                                    rx.list_item(
                                        rx.link(
                                            "Machine Learning con Python",
                                            href=routes.urls.PLAT_ML,
                                            is_external=True,
                                        ),
                                        style={"font-size": "14px"},
                                    ),
                                    rx.list_item(
                                        rx.link(
                                            "Data e IA",
                                            href=routes.urls.PLAT_IA,
                                            is_external=True,
                                        ),
                                    ),  style={"font-size": "14px"},
                                ),
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        as_child=True,
                        width="100%",
                    ),
                    orientation="vertical",
                    spacing="4",
                ),
            ),
            collapse=True,
            orientation="vertical",
            width="100%",
            variant="outline",
            radius="medium",
        )
    )


@rx.page(route=routes.urls.PROFILE)
def profile_page() -> rx.Component:
    my_child = rx.container(
        rx.vstack(
            profile_content(),
            profile_description(),
            spacing="5",
            align="center",
            min_height="85vh",
            id="my-child",
        )
    )
    return base_page(my_child)
