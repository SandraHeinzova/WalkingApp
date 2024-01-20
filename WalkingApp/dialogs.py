import flet as ft


##################
# Event Handlers #
##################
def show_confirm_dialog(page):
    """every control that belongs to the confirm dialog - when user wants to exit application
    :param page: container for controls in View"""
    def yes_click(_):
        """exits the app"""
        page.window_destroy()

    def no_click(_):
        """goes back into the app"""
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
    """every control that belongs to the incomplete dialog - when user forget to fill one of the
    text fields
    :param page: container for controls in View"""
    def return_back(_):
        """goes back into the app, so user can fill forgotten text fields"""
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
    """every control that belongs to the wrong time dialog - when user fill in wrong format of the time
    :param page: container for controls in View"""
    def fix_time(_):
        """goes back into the app, so user can fill time in right format"""
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


def show_success_dialogue(page, fill_func, table):
    """every control that belongs to the success dialog - when user fill in everything correctly
    and application successfully saved it to the Excel
    :param page: container for controls in View
    :param fill_func: function for filling the data table with updated data
    :param table: the data table to be filled"""
    def success(_):
        """launches the fill_func and goes back to the app"""
        success_dialog.open = False
        fill_func(page, table)
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
    """every control that belongs to the no date picked dialog - when user forgets to pick a date
    :param page: container for controls in View"""
    def go_pick_date(_):
        """goes back into the app, so user can pick a date"""
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
