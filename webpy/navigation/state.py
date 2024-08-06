import reflex as rx

from . import routes


class NavState(rx.State):
    
    def to_home_page(self):
        return rx.redirect(routes.HOME_ROUTE)
    
    def to_about_page(self):
        return rx.redirect(routes.ABOUT_ROUTE)

    def to_contact_page(self):
        return rx.redirect(routes.CONTACT_ROUTE)