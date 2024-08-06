import reflex as rx

from . ui.base import base_page

from . import pages, navigation

class State(rx.State):
    """The app state."""
    label:str = "MAUFRANZAR"
    
    def handle_title_input_change(self, val):
        self.label = val
        
    def did_click(self):
        print("Clicked!!")
        return rx.redirect(navigation.routes.HOME_ROUTE)
      


def index() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading(State.label,size="9"),
            rx.link(
                rx.button("About"),
                href=navigation.routes.ABOUT_ROUTE,
            ),
            rx.link(
                rx.button("contact"),
                href=navigation.routes.CONTACT_ROUTE,
            ),
            spacing="5",
            justify="center",
            align="center",
            text_align="center",
            min_height="85vh",
            id="my-child",
        )
    return base_page(my_child)



app = rx.App()
app.add_page(
    index,
    title="maufranzar",
    description="web personal de maufranzar",
    image="/img/logo_.ico",
)
app.add_page(pages.about_page, route=navigation.routes.ABOUT_ROUTE)
app.add_page(pages.contact_page, route=navigation.routes.CONTACT_ROUTE)
