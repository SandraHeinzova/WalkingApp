import flet as ft
import excel_func


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

