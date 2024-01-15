import flet as ft
import excel_func


def fill_recent_walks_table(page):
    walks_data = excel_func.get_recent_walks()
    recent_walks = walks_data if walks_data else [("Žádné záznamy", "")]
    data_table.rows = [
        ft.DataRow(
            [ft.DataCell(ft.Text(date)), ft.DataCell(ft.Text(kms))]
        ) for date, kms in recent_walks]
    page.update()


def exit_button_create(func_exit):
    exit_button = ft.ElevatedButton(text="Konec",
                                    style=ft.ButtonStyle(
                                        shape=ft.ContinuousRectangleBorder(radius=30)),
                                    on_click=func_exit)
    return exit_button


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
