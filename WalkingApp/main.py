import flet as ft
from datetime import datetime
import re
import dialogs
import excel_func
import statistics

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

    def fill_recent_walks_table():
        walks_data = excel_func.get_recent_walks()
        recent_walks = walks_data if walks_data else [("Žádné záznamy", "")]
        data_table.rows = [
            ft.DataRow(
                [ft.DataCell(ft.Text(date)), ft.DataCell(ft.Text(kms))]
            ) for date, kms in recent_walks]
        page.update()

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
        if not all([walked_time_entry.value, walked_kms_entry.value, walked_kcal_entry.value,
                    walked_steps_entry.value]):
            dialogs.show_incomplete_dialog(page)
            return

        if not date_picker.value:
            page.go("/")
            dialogs.show_no_date_picked_dialog(page)
            return

        date = date_picker.value.strftime("%d/%m/%y")
        kms = float(walked_kms_entry.value)
        time = save_time_entry(walked_time_entry.value)
        kcal = int(walked_kcal_entry.value)
        steps = int(walked_steps_entry.value)

        if time is None:
            return

        excel_func.save_to_excel(date, kms, time, kcal, steps)

        dialogs.show_success_dialogue(page, fill_recent_walks_table)

        walked_kms_entry.value = ""
        walked_time_entry.value = ""
        walked_kcal_entry.value = ""
        walked_steps_entry.value = ""
        page.update()

    # CONTROLS OF THE APP - BUTTONS, TEXTS

    welcome_txt = ft.Text(value="\nVítej ve WalkingApp!\n",
                          color=ft.colors.INDIGO,
                          style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                          text_align=ft.TextAlign.CENTER)

    walked_kms_entry = ft.TextField(label="Kolik jsi ušel?",
                                    hint_text="km.m",
                                    width=160,
                                    border_radius=0,
                                    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9.]",
                                                                replacement_string=""),
                                    keyboard_type=ft.KeyboardType.NUMBER)
    walked_time_entry = ft.TextField(label="Za jak dlouho?",
                                     hint_text="hodiny:minuty",
                                     width=160,
                                     border_radius=0,
                                     input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9:]",
                                                                 replacement_string=""))
    walked_kcal_entry = ft.TextField(label="Kolik kalorií?",
                                     width=160,
                                     border_radius=0,
                                     input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]",
                                                                 replacement_string=""),
                                     keyboard_type=ft.KeyboardType.NUMBER)
    walked_steps_entry = ft.TextField(label="A kolik kroků?",
                                      width=160,
                                      border_radius=0,
                                      input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]",
                                                                  replacement_string=""),
                                      keyboard_type=ft.KeyboardType.NUMBER)

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

    data_table = ft.DataTable(
        bgcolor=ft.colors.WHITE54,
        columns=[
            ft.DataColumn(ft.Text("Datum")),
            ft.DataColumn(ft.Text("Kilometry")),
        ],
        rows=[]
    )

    new_record_button = ft.FilledButton(text="Přidej nový záznam",
                                        on_click=lambda _: page.go("/new"))

    exit_button = ft.ElevatedButton(text="Konec",
                                    style=ft.ButtonStyle(
                                        shape=ft.ContinuousRectangleBorder(radius=30)),
                                    on_click=window_event)

    save_button = ft.ElevatedButton(text="Uložit",
                                    on_click=save_clicked)

    show_statistics_button = ft.ElevatedButton(text="Ukaž statistiky",
                                               on_click=open_statistics)

    fill_recent_walks_table()
    page.overlay.append(date_picker)

    open_maps = ft.Chip(
        label=ft.Text("Nápad na trasu"),
        leading=ft.Icon(ft.icons.MAP_SHARP),
        on_click=open_google_maps,
    )

    # GUI OF THE APP

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
            page.views.append(
                ft.View(
                    route="/new",
                    bgcolor=ft.colors.BLUE_100,
                    padding=0,
                    appbar=ft.AppBar(title=ft.Text("Nový záznam"),
                                     bgcolor=ft.colors.BLUE_100),
                    controls=[
                        ft.Stack(controls=[
                            ft.Image(
                                src="https://picsum.photos/id/651/400/800",
                                width=page.window_width,
                                height=page.window_height,
                                fit=ft.ImageFit.FILL),
                            ft.Container(content=walked_kms_entry,
                                         top=30,
                                         left=25,
                                         bgcolor=ft.colors.BLUE_50),
                            ft.Container(content=walked_time_entry,
                                         top=30,
                                         left=200,
                                         bgcolor=ft.colors.BLUE_50),
                            ft.Container(content=walked_kcal_entry,
                                         top=110,
                                         left=25,
                                         bgcolor=ft.colors.BLUE_50),
                            ft.Container(content=walked_steps_entry,
                                         top=110,
                                         left=200,
                                         bgcolor=ft.colors.BLUE_50),
                            ft.Container(content=save_button,
                                         top=200,
                                         left=20),
                            ft.Container(content=show_statistics_button,
                                         left=20,
                                         top=250),
                            ft.Container(content=data_table,
                                         left=70,
                                         top=350),
                            ft.Container(content=exit_button,
                                         right=5,
                                         bottom=80,
                                         width=100,
                                         height=25),

                        ],
                            width=page.window_width,
                            height=page.window_height - 70)]
                )
            )

        if page.route == "/statistics":
            page.views.append(statistics.route_statistics(page, window_event))
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
