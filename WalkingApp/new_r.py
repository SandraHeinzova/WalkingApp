import flet as ft
import controls


def save_button_create(func_save):
    save_button = ft.ElevatedButton(text="Uložit",
                                    on_click=func_save)
    return save_button


def show_stat_button_create(func_stat):
    show_statistics_button = ft.ElevatedButton(text="Ukaž statistiky",
                                               on_click=func_stat)
    return show_statistics_button


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


def route_new(page, func_save, func_stat, func_exit):
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
                            ft.Container(content=save_button_create(func_save),
                                         top=200,
                                         left=20),
                            ft.Container(content=show_stat_button_create(func_stat),
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
