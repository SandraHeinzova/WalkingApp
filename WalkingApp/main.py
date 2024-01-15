import flet as ft
from datetime import datetime
import re
import dialogs
import excel_func
import statistics_r
import new_r
import controls

pattern_hours_minutes = r'^([0-9]|1[0-2]|2[0-3]):[0-5][0-9]$'
pattern_hours = r'^(1?[0-9]|2[0-3])$'


# MAIN BODY OF THE APP WRAP IN FUNCTION MAIN
def main(page: ft.Page):
    page.title = "WalkingApp"
    page.padding = 0
    page.window_width = 400
    page.window_height = 850
    page.bgcolor = ft.colors.BLUE_100
    page.window_resizable = False
    page.window_maximizable = False
    page.theme_mode = ft.ThemeMode.LIGHT

    def window_event(e):
        if e.data == "close" or e.name == "click":
            dialogs.show_confirm_dialog(page)

    page.window_prevent_close = True
    page.on_window_event = window_event

    def open_statistics(_):
        page.go("/statistics")

    def pick_date(_):
        picked_date.value = "Budeš přidávat aktivitu ze dne {}".format(date_picker.value.strftime("%d/%m/%y"))
        page.update()

    def open_google_maps(_):
        page.launch_url("https://mapy.cz/")

    def save_time_entry(walked_time_entry_value):
        if re.search(pattern_hours_minutes, walked_time_entry_value):
            time_format_to_save = f"{walked_time_entry_value}:00"
            return time_format_to_save
        elif re.search(pattern_hours, walked_time_entry_value):
            time_format_to_save = f"{walked_time_entry_value}:00:00"
            return time_format_to_save
        else:
            dialogs.show_wrong_time_dialog(page)
            return None

    def save_clicked(_):
        if not all([controls.walked_time_entry.value, controls.walked_kms_entry.value, controls.walked_kcal_entry.value,
                    controls.walked_steps_entry.value]):
            dialogs.show_incomplete_dialog(page)
            return

        if not date_picker.value:
            page.go("/")
            dialogs.show_no_date_picked_dialog(page)
            return

        date = date_picker.value.strftime("%d/%m/%y")
        kms = float(controls.walked_kms_entry.value)
        time = save_time_entry(controls.walked_time_entry.value)
        kcal = int(controls.walked_kcal_entry.value)
        steps = int(controls.walked_steps_entry.value)

        if time is None:
            return

        excel_func.save_to_excel(date, kms, time, kcal, steps)

        dialogs.show_success_dialogue(page, controls.fill_recent_walks_table)

        controls.walked_kms_entry.value = ""
        controls.walked_time_entry.value = ""
        controls.walked_kcal_entry.value = ""
        controls.walked_steps_entry.value = ""
        page.update()

    # CONTROLS OF THE APP - BUTTONS, TEXTS

    welcome_txt = ft.Text(value="\nVítej ve WalkingApp!\n",
                          color=ft.colors.INDIGO,
                          style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                          text_align=ft.TextAlign.CENTER)



    date_picker = ft.DatePicker(on_change=pick_date,
                                first_date=datetime(2023, 10, 1),
                                last_date=datetime(2030, 12, 31)
                                )

    date_button = ft.ElevatedButton("Vyber datum",
                                    icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                                    on_click=lambda _: date_picker.pick_date(),
                                    )
    picked_date = ft.Text(value="Vyber datum",
                          text_align=ft.TextAlign.CENTER,
                          color=ft.colors.WHITE54)

    new_record_button = ft.FilledButton(text="Přidej nový záznam",
                                        on_click=lambda _: page.go("/new"))

    exit_button = ft.ElevatedButton(text="Konec",
                                    style=ft.ButtonStyle(
                                        shape=ft.ContinuousRectangleBorder(radius=30)),
                                    on_click=window_event)

    page.overlay.append(date_picker)

    open_maps = ft.Chip(
        label=ft.Text("Nápad na trasu"),
        leading=ft.Icon(ft.icons.MAP_SHARP),
        on_click=open_google_maps,
    )

    # GUI OF THE APP
    controls.fill_recent_walks_table(page)

    def views(_):
        page.views.clear()
        page.views.append(
            ft.View(
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
                                     content=new_record_button),
                        ft.Container(right=90,
                                     bottom=195,
                                     width=200,
                                     height=50,
                                     content=open_maps),
                        ft.Container(right=5,
                                     bottom=80,
                                     width=100,
                                     height=25,
                                     content=exit_button),
                    ],
                    width=page.window_width,
                    height=page.window_height)],
            )
        )
        if page.route == "/new" or page.route == "/statistics":
            page.views.append(new_r.route_new(page, save_clicked, open_statistics, window_event))

        if page.route == "/statistics":
            page.views.append(statistics_r.route_statistics(page, window_event))
        page.update()

    def view_pop(_):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = views
    page.on_view_pop = view_pop
    page.go(page.route)


# START OF THE APP

ft.app(target=main)
