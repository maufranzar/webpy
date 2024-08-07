import reflex as rx

from . import urls



class NavState(rx.State):
    def to_home(self):
        return rx.redirect(urls.HOME)
    
    def to_contact(self):
        return rx.redirect(urls.CONTACT)
    
    def to_profile(self):
        return rx.redirect(urls.PROFILE)