import flet as ft
import excel_func
import re
import dialogs

pattern_hours_minutes = r'^([0-9]|1[0-2]|2[0-3]):[0-5][0-9]$'
pattern_hours = r'^(1?[0-9]|2[0-3])$'


def fill_recent_walks_table(page, table):
    walks_data = excel_func.get_recent_walks()
    recent_walks = walks_data if walks_data else [("Žádné záznamy", "")]
    table.rows = [
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
