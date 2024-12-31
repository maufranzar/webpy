# webpy/pages/projects.py

import reflex as rx

from ..components.base import base_page
from .. import routes


def feature_item(feature: str) -> rx.Component:
    """
    Crea un ítem de característica con un ícono de check y texto.
    """
    return rx.hstack(
        rx.icon("check", color=rx.color("green", 9), size=21),
        rx.text(feature, size="4", weight="regular"),
    )


def iot_features() -> rx.Component:
    """
    Características destacadas del proyecto IoT con ESP32 y LoRa.
    """
    return rx.vstack(
        feature_item("Sistema IoT con ESP32"),
        feature_item("Monitoreo en tiempo real de sensores"),
        feature_item("Comunicación LoRa de largo alcance"),
        spacing="3",
        width="100%",
        align_items="start",  # Alinea íconos y texto a la izquierda
    )


def cnn_features() -> rx.Component:
    """
    Características destacadas del proyecto de Red Neuronal Híbrida CNN+LSTM.
    """
    return rx.vstack(
        feature_item("Modelo híbrido CNN+LSTM"),
        feature_item("Análisis de señales de audio"),
        feature_item("Detección de patrones armónicos complejos"),
        spacing="3",
        width="100%",
        align_items="start",  # Alinea íconos y texto a la izquierda
    )


def project_card_iot() -> rx.Component:
    """
    Tarjeta que muestra información del proyecto 'Monitoreo de equipos con ESP32 y LoRa'.
    Reemplazamos la imagen por un ícono.
    """
    return rx.vstack(
        # Título del proyecto
        rx.text(
            "Monitoreo de Equipos y Sensores con ESP32 y LoRa",
            weight="bold",
            size="5",
            width="100%",
            text_align="left",
        ),
        # Ícono representativo (por ejemplo: 'wifi-high' de Phosphor)
        rx.box(
            display="flex",
            justify_content="center",
            width="100%",
        ),
        # Lista de características
        iot_features(),
        rx.spacer(),
        # Botón centrado
        rx.box(
            rx.link(
                rx.button(
                    "Ver Detalles",
                    size="3",
                    color_scheme="blue",
                    width="auto",
                ),
                href=routes.urls.GITHUB_IOT,  # Ajusta a tu enlace
                is_external=True,
            ),
            display="flex",
            justify_content="center",
            width="100%",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('blue', 6)}",
        background=rx.color("blue", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )


def project_card_cnn() -> rx.Component:
    """
    Tarjeta que muestra información del proyecto
    'Análisis de Patrones Musicales con Redes Neuronales'.
    Reemplazamos la imagen por un ícono.
    """
    return rx.vstack(
        # Título del proyecto
        rx.text(
            "Análisis de Patrones Armónicos con Redes Neuronales",
            weight="bold",
            size="5",
            width="100%",
            text_align="left",
        ),
        # Ícono representativo (por ejemplo: 'music-notes-simple' de Phosphor)
        rx.box(
            display="flex",
            justify_content="center",
            width="100%",
        ),
        # Lista de características
        cnn_features(),
        rx.spacer(),
        # Botón centrado
        rx.box(
            rx.link(
                rx.button(
                    "Ver Detalles",
                    size="3",
                    color_scheme="blue",
                    width="auto",
                ),
                href=routes.urls.GITHUB_NN,  # Ajusta a tu enlace
                is_external=True,
            ),
            display="flex",
            justify_content="center",
            width="100%",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('blue', 6)}",
        background=rx.color("blue", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )


@rx.page(route=routes.urls.PROJECTS)
def projects_page() -> rx.Component:
    """
    Página que agrupa los proyectos en un layout centrado.
    """
    my_child = rx.hstack(
        project_card_iot(),
        project_card_cnn(),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id="my-child",
    )
    return base_page(my_child)
