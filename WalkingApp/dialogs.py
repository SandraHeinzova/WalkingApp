import flet as ft
import model


def _close_dialog(page, dlg):
    dlg.open = False
    page.update()


def _clear_table_and_statistics(page, dlg):
    model.reset_database()
    _close_dialog(page, dlg)


def show_confirm_exit_dialog(page):
    confirm_exit_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Potvrzení"),
        content=ft.Text("Opravdu si přeješ apku ukončit?"),
        actions=[
            ft.ElevatedButton("Ano", on_click=lambda _: page.window_destroy()),
            ft.ElevatedButton("Ne", on_click=lambda _: _close_dialog(page, confirm_exit_dialog)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        open=True,
    )

    page.dialog = confirm_exit_dialog
    page.update()


def show_required_fields_missing_dialog(page):
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


def show_confirm_deleting_records_dialog(page):
    confirm_deleting_records_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Opravdu vše smazat?"),
        content=ft.Text("Tato akce nenávratně vymaže všechny záznamy.\nPřeješ si pokračovat?"),
        actions=[
            ft.ElevatedButton("Ano", on_click=lambda _:
                                          _clear_table_and_statistics(page, confirm_deleting_records_dialog)),
            ft.ElevatedButton("Ne", on_click=lambda _: _close_dialog(page, confirm_deleting_records_dialog)),
        ],
        open=True,
    )

    page.dialog = confirm_deleting_records_dialog
    page.update()
