import flet as ft
import dialogs


##################
# Event Handlers #
##################
def _changing_route(index, e):
    if index == 0:
        return e.page.go("/")
    if index == 1:
        return e.page.go("/new")
    if index == 2:
        return e.page.go("/statistics")
    if index == 3:
        return dialogs.show_confirm_exit_dialog(e.page)


###########
#  View   #
###########
nav_bar = ft.NavigationBar(
            bgcolor=ft.colors.BLUE_100,
            on_change=lambda e: _changing_route(e.control.selected_index, e),
            destinations=[
                ft.NavigationDestination(icon=ft.icons.HOME_ROUNDED, label="Domů"),
                ft.NavigationDestination(icon=ft.icons.POST_ADD, label="Nový záznam"),
                ft.NavigationDestination(icon=ft.icons.INSERT_CHART_ROUNDED, label="Statistiky"),
                ft.NavigationDestination(icon=ft.icons.LOGOUT, label="Konec")
            ])
