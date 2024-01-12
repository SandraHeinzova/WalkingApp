import flet as ft


def show_confirm_dialog(page):
    def yes_click(_):
        page.window_destroy()

    def no_click(_):
        confirm_dialog.open = False
        page.update()

    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Potvrzení"),
        content=ft.Text("Opravdu si přeješ apku ukončit?"),
        actions=[
            ft.ElevatedButton("Ano", on_click=yes_click),
            ft.ElevatedButton("Ne", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        open=True,
    )

    page.dialog = confirm_dialog
    page.update()


def show_incomplete_dialog(page):
    def return_back(_):
        incomplete_dialog.open = False
        page.update()

    incomplete_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Něco jsi zapomněl"),
        content=ft.Text("Vše musí být vyplněno"),
        actions=[
            ft.ElevatedButton("OK, doplním", on_click=return_back)
        ],
        open=True,
    )

    page.dialog = incomplete_dialog
    page.update()


def show_wrong_time_dialog(page):
    def fix_time(_):
        wrong_time_dialog.open = False
        page.update()

    wrong_time_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Špatný formát času"),
        content=ft.Text("Zadej prosím celé hodiny, nebo hodiny a minuty."),
        actions=[
            ft.ElevatedButton("OK", on_click=fix_time)
        ],
        open=True,
    )

    page.dialog = wrong_time_dialog
    page.update()


def show_success_dialogue(page, fill_func):
    def success(_):
        success_dialog.open = False
        fill_func()
        page.update()

    success_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Úspěch"),
        content=ft.Text("Vše bylo úspěšně zapsáno"),
        actions=[
            ft.ElevatedButton("OK", on_click=success)
        ],
        open=True,
    )

    page.dialog = success_dialog
    page.update()


def show_no_date_picked_dialog(page):
    def go_pick_date(_):
        no_date_picked_dialog.open = False
        page.update()

    no_date_picked_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Chybí vybrané datum"),
        content=ft.Text("Vyber datum prosím"),
        actions=[
            ft.ElevatedButton("Jdu vybrat", on_click=go_pick_date)
        ],
        open=True,
    )

    page.dialog = no_date_picked_dialog
    page.update()