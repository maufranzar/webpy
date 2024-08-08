import reflex as rx



def link_icon(image:str, url:str, alt:str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            #width="50px",
            alt = alt,
        ),
        href=url,
        is_external=True
    )
    
def link_button(title:str, image:str ,body:str, url:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width="50px",
                    height="50px",
                    margin="5px",
                    alt = title
                ),
                rx.vstack(
                    rx.heading(title),
                    rx.text(body),
                    align_items="start",
                    justify="center",
                ),
                width="100%",
            ),
            # 
        ),
        href=url,
        is_external=True,
        width="100%"
    )