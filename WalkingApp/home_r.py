import flet as ft
from datetime import datetime
import model
import routing


###########
#  View   #
###########
# textfield that shows welcome text
_welcome_txt = ft.Text(value="\nVítej ve WalkingApp!\n",
                       color=ft.colors.INDIGO,
                       theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                       text_align=ft.TextAlign.CENTER)

# textfield that shows the date picked by the user
_picked_date = ft.Text(value="Vyber datum",
                       text_align=ft.TextAlign.CENTER,
                       color=ft.colors.WHITE54)

# control that opens maps in the browser
_open_maps = ft.Chip(
    label=ft.Text("Nápad na trasu"),
    leading=ft.Icon(ft.icons.MAP_SHARP),
    on_click=lambda e: e.page.launch_url("https://mapy.cz/"),
)


###########
#  Route  #
###########
def create_home_view(page):
    """Return the view for the '/' route
    :param page: container for controls in View"""
    view_home = ft.View(
        "/",
        bgcolor=ft.colors.BLUE_100,
        padding=0,
        navigation_bar=routing.nav_bar,
        controls=[ft.Stack(
            [
                ft.Image(
                    src="https://picsum.photos/id/651/400/800",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.FILL
                ),
                ft.Container(top=-10,
                             left=65,
                             height=200,
                             width=270,
                             content=_welcome_txt),
                ft.Container(right=100,
                             top=280,
                             width=180,
                             height=35,
                             content=_open_maps),
            ],
            width=page.window_width,
            height=page.window_height - 70)],
    )
    return view_home
