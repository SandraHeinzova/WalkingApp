import flet as ft
import re
import home_r
import controls
import dialogs
import excel_func

pattern_hours_minutes = r'^([0-9]|1[0-2]|2[0-3]):[0-5][0-9]$'
pattern_hours = r'^(1?[0-9]|2[0-3])$'


def open_statistics(e):
    e.page.go("/statistics")


def save_time_entry(page, walked_time_entry_value):
    if re.search(pattern_hours_minutes, walked_time_entry_value):
        time_format_to_save = f"{walked_time_entry_value}:00"
        return time_format_to_save
    elif re.search(pattern_hours, walked_time_entry_value):
        time_format_to_save = f"{walked_time_entry_value}:00:00"
        return time_format_to_save
    else:
        dialogs.show_wrong_time_dialog(page)
        return None


def save_clicked(e, page):
    if not all([walked_time_entry.value, walked_kms_entry.value, walked_kcal_entry.value,
                walked_steps_entry.value]):
        dialogs.show_incomplete_dialog(page)
        return

    if not home_r.date_picker.value:
        e.page.go("/")
        dialogs.show_no_date_picked_dialog(page)
        return

    date = home_r.date_picker.value.strftime("%d/%m/%y")
    kms = float(walked_kms_entry.value)
    time = save_time_entry(page, walked_time_entry.value)
    kcal = int(walked_kcal_entry.value)
    steps = int(walked_steps_entry.value)

    if time is None:
        return

    excel_func.save_to_excel(date, kms, time, kcal, steps)

    dialogs.show_success_dialogue(page, controls.fill_recent_walks_table, data_table)

    walked_kms_entry.value = ""
    walked_time_entry.value = ""
    walked_kcal_entry.value = ""
    walked_steps_entry.value = ""
    page.update()


def save_button_create(e, page):
    save_button = ft.ElevatedButton(text="Uložit",
                                    on_click=lambda _: save_clicked(e, page))
    return save_button


show_statistics_button = ft.ElevatedButton(text="Ukaž statistiky",
                                           on_click=open_statistics)

data_table = ft.DataTable(
    bgcolor=ft.colors.WHITE54,
    columns=[
        ft.DataColumn(ft.Text("Datum")),
        ft.DataColumn(ft.Text("Kilometry")),
    ],
    rows=[])

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


def route_new(page, func_exit):
    view_new = ft.View(
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
                ft.Container(content=save_button_create("e", page),
                             top=200,
                             left=20),
                ft.Container(content=show_statistics_button,
                             left=20,
                             top=250),
                ft.Container(content=data_table,
                             left=70,
                             top=350),
                ft.Container(content=controls.exit_button_create(func_exit),
                             right=5,
                             bottom=80,
                             width=100,
                             height=25)
            ],
                width=page.window_width,
                height=page.window_height - 70)]
    )

    return view_new
