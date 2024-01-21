import flet as ft


def _close_dialog(page, dlg):
    """goes back into the app"""
    dlg.open = False
    page.update()


def show_confirm_exit_dialog(page):
    """every control that belongs to the confirm exit dialog - when user wants to exit application
    :param page: container for controls in View"""
    def exit_app(_):
        page.window_destroy()

    confirm_exit_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Potvrzení"),
        content=ft.Text("Opravdu si přeješ apku ukončit?"),
        actions=[
            ft.ElevatedButton("Ano", on_click=exit_app),
            ft.ElevatedButton("Ne", on_click=lambda _: _close_dialog(page, confirm_exit_dialog)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        open=True,
    )

    page.dialog = confirm_exit_dialog
    page.update()


def show_required_fields_missing_dialog(page):
    """every control that belongs to the required fields missing dialog - when user forget to fill one of the
    text fields
    :param page: container for controls in View"""

    required_fields_missing_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Něco jsi zapomněl"),
        content=ft.Text("Vše musí být vyplněno"),
        actions=[
            ft.ElevatedButton("OK, doplním", on_click=lambda _: _close_dialog(page, required_fields_missing_dialog))
        ],
        open=True,
    )

    page.dialog = required_fields_missing_dialog
    page.update()


def show_invalid_time_format_dialog(page):
    """every control that belongs to the invalid format time dialog - when user fill in wrong format of the time
    :param page: container for controls in View"""

    invalid_time_format_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Špatný formát času"),
        content=ft.Text("Zadej prosím celé hodiny, nebo hodiny a minuty."),
        actions=[
            ft.ElevatedButton("OK", on_click=lambda _: _close_dialog(page, invalid_time_format_dialog))
        ],
        open=True,
    )

    page.dialog = invalid_time_format_dialog
    page.update()


def show_entry_saved_success_dialog(page):
    """every control that belongs to the entry saved success dialog - when user fill in everything correctly
    and application successfully saved it to the Excel
    :param page: container for controls in View"""

    entry_saved_success_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Úspěch"),
        content=ft.Text("Vše bylo úspěšně zapsáno"),
        actions=[
            ft.ElevatedButton("OK", on_click=lambda _: _close_dialog(page, entry_saved_success_dialog))
        ],
        open=True,
    )

    page.dialog = entry_saved_success_dialog
    page.update()


def show_no_date_picked_dialog(page):
    """every control that belongs to the no date picked dialog - when user forgets to pick a date
    :param page: container for controls in View"""

    no_date_picked_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Chybí vybrané datum"),
        content=ft.Text("Vyber datum prosím"),
        actions=[
            ft.ElevatedButton("Jdu vybrat", on_click=lambda _: _close_dialog(page, no_date_picked_dialog))
        ],
        open=True,
    )

    page.dialog = no_date_picked_dialog
    page.update()
