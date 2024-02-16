import flet as ft
from datetime import datetime
import model
import routing


##################
# Event Handlers #
##################
def _update_picked_date(e):
    model.selected_date = _date_picker.value.strftime("%d/%m/%y")
    _picked_date.value = "Budeš přidávat aktivitu ze dne {}".format(model.selected_date)
    e.page.update()


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

# button that opens calendar to pick a date
_date_button = ft.ElevatedButton("Vyber datum",
                                 icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                                 on_click=lambda _: _date_picker.pick_date())

# date picker control - calendar to choose date
_date_picker = ft.DatePicker(on_change=_update_picked_date,
                             first_date=datetime(2023, 10, 1),
                             last_date=datetime(2030, 12, 31))

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
    if _date_picker not in page.overlay:
        page.overlay.append(_date_picker)
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
                ft.Container(left=65,
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
