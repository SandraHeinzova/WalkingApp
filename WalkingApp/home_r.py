import flet as ft
import controls
from datetime import datetime

welcome_txt = ft.Text(value="\nVítej ve WalkingApp!\n",
                      color=ft.colors.INDIGO,
                      style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                      text_align=ft.TextAlign.CENTER)

picked_date = ft.Text(value="Vyber datum",
                      text_align=ft.TextAlign.CENTER,
                      color=ft.colors.WHITE54)

date_button = ft.ElevatedButton("Vyber datum",
                                icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                                on_click=lambda _: date_picker.pick_date())


def pick_date(e):
    picked_date.value = "Budeš přidávat aktivitu ze dne {}".format(date_picker.value.strftime("%d/%m/%y"))
    e.page.update()


date_picker = ft.DatePicker(on_change=pick_date,
                            first_date=datetime(2023, 10, 1),
                            last_date=datetime(2030, 12, 31))


def new_record_button_create(page):
    new_record_button = ft.FilledButton(text="Přidej nový záznam",
                                        on_click=lambda _: page.go("/new"))
    return new_record_button


def open_czech_maps(e):
    e.page.launch_url("https://mapy.cz/")


open_maps = ft.Chip(
    label=ft.Text("Nápad na trasu"),
    leading=ft.Icon(ft.icons.MAP_SHARP),
    on_click=open_czech_maps,
)


def route_home(page, func_exit):
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
                                     content=controls.exit_button_create(func_exit)),
                    ],
                    width=page.window_width,
                    height=page.window_height)],
            )
    return view_home