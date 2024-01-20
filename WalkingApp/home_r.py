import flet as ft
from datetime import datetime
import model


##################
# Event Handlers #
##################
def pick_date(e):
    """updates picked_date value
    :param e: event"""
    picked_date.value = "Budeš přidávat aktivitu ze dne {}".format(date_picker.value.strftime("%d/%m/%y"))
    date_button.text = date_picker.value.strftime("%d/%m/%y")
    model.selected_date = date_picker.value.strftime("%d/%m/%y")
    e.page.update()


def new_record_button_create(page):
    """creates a button that redirects to the page "/new", to add new record
    :param page: container for controls in View"""
    new_record_button = ft.FilledButton(text="Přidej nový záznam",
                                        on_click=lambda _: page.go("/new"))
    return new_record_button


def exit_button_create(func_exit):
    """creates a button that exits application
     :param func_exit: function that exits an app"""
    exit_button = ft.ElevatedButton(text="Konec",
                                    style=ft.ButtonStyle(
                                        shape=ft.ContinuousRectangleBorder(radius=30)),
                                    on_click=func_exit)
    return exit_button


def open_czech_maps(e):
    """opens maps - to check where is possible to go for a walk
    :param e: event"""
    e.page.launch_url("https://mapy.cz/")


###########
#  View   #
###########
# textfield that shows welcome text
welcome_txt = ft.Text(value="\nVítej ve WalkingApp!\n",
                      color=ft.colors.INDIGO,
                      style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                      text_align=ft.TextAlign.CENTER)

# textfield that shows which date hase user picked from date_picker, to check if it's correct
picked_date = ft.Text(value="Vyber datum",
                      text_align=ft.TextAlign.CENTER,
                      color=ft.colors.WHITE54)

# button that opens calendar to pick a date
date_button = ft.ElevatedButton("Vyber datum",
                                icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                                on_click=lambda _: date_picker.pick_date())


# date picker control - calendar to choose date
date_picker = ft.DatePicker(on_change=pick_date,
                            first_date=datetime(2023, 10, 1),
                            last_date=datetime(2030, 12, 31))


# control that activate open_czech_maps function
open_maps = ft.Chip(
    label=ft.Text("Nápad na trasu"),
    leading=ft.Icon(ft.icons.MAP_SHARP),
    on_click=open_czech_maps,
)


###########
#  Route  #
###########
def route_home(page, func_exit):
    """route to '/'
    :param page: container for controls in View
    :param func_exit: function for exiting an app"""
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
                                     content=welcome_txt),
                        ft.Container(right=100,
                                     top=280,
                                     width=180,
                                     height=35,
                                     content=date_button),
                        ft.Container(right=90,
                                     top=325,
                                     height=50,
                                     width=200,
                                     content=picked_date),
                        ft.Container(right=90,
                                     top=420,
                                     width=200,
                                     height=30,
                                     content=new_record_button_create(page)),
                        ft.Container(right=90,
                                     bottom=195,
                                     width=200,
                                     height=50,
                                     content=open_maps),
                        ft.Container(right=5,
                                     bottom=80,
                                     width=100,
                                     height=25,
                                     content=exit_button_create(func_exit)),
                    ],
                    width=page.window_width,
                    height=page.window_height)],
            )
    return view_home
