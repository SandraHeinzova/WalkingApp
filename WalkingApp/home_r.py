import flet as ft
from datetime import datetime
import model
import dialogs


##################
# Event Handlers #
##################
def _pick_date(e):
    """updates picked_date value
    :param e: event"""
    _picked_date.value = "Budeš přidávat aktivitu ze dne {}".format(_date_picker.value.strftime("%d/%m/%y"))
    _date_button.text = _date_picker.value.strftime("%d/%m/%y")
    model.selected_date = _date_picker.value.strftime("%d/%m/%y")
    e.page.update()


def _new_record_button_create(page):
    """creates a button that redirects to the page "/new", to add new record
    :param page: container for controls in View"""
    new_record_button = ft.FilledButton(text="Přidej nový záznam",
                                        on_click=lambda _: page.go("/new"))
    return new_record_button


def _exit_button_create():
    """creates a button that exits application"""
    exit_button = ft.ElevatedButton(text="Konec",
                                    style=ft.ButtonStyle(
                                        shape=ft.ContinuousRectangleBorder(radius=30)),
                                    on_click=lambda e: dialogs.show_confirm_dialog(e.page))
    return exit_button


def _open_czech_maps(e):
    """opens maps - to check where is possible to go for a walk
    :param e: event"""
    e.page.launch_url("https://mapy.cz/")


###########
#  View   #
###########
# textfield that shows welcome text
_welcome_txt = ft.Text(value="\nVítej ve WalkingApp!\n",
                       color=ft.colors.INDIGO,
                       style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                       text_align=ft.TextAlign.CENTER)

# textfield that shows which date hase user picked from date_picker, to check if it's correct
_picked_date = ft.Text(value="Vyber datum",
                       text_align=ft.TextAlign.CENTER,
                       color=ft.colors.WHITE54)

# button that opens calendar to pick a date
_date_button = ft.ElevatedButton("Vyber datum",
                                 icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                                 on_click=lambda _: _date_picker.pick_date())

# date picker control - calendar to choose date
_date_picker = ft.DatePicker(on_change=_pick_date,
                             first_date=datetime(2023, 10, 1),
                             last_date=datetime(2030, 12, 31))

# control that activate open_czech_maps function
_open_maps = ft.Chip(
    label=ft.Text("Nápad na trasu"),
    leading=ft.Icon(ft.icons.MAP_SHARP),
    on_click=_open_czech_maps,
)


###########
#  Route  #
###########
def route_home(page):
    """route to '/'
    :param page: container for controls in View"""
    view_home = ft.View(
        "/",
        bgcolor=ft.colors.BLUE_100,
        padding=0,
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
                             content=_date_button),
                ft.Container(right=90,
                             top=325,
                             height=50,
                             width=200,
                             content=_picked_date),
                ft.Container(right=90,
                             top=420,
                             width=200,
                             height=30,
                             content=_new_record_button_create(page)),
                ft.Container(right=90,
                             bottom=195,
                             width=200,
                             height=50,
                             content=_open_maps),
                ft.Container(right=5,
                             bottom=80,
                             width=100,
                             height=25,
                             content=_exit_button_create()),
            ],
            width=page.window_width,
            height=page.window_height)],
    )
    return view_home
