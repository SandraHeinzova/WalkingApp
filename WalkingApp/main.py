import flet as ft
import dialogs
import statistics_r
import new_entry_r
import home_r


def main(page: ft.Page):
    """the applications entry point"""
    page.title = "WalkingApp"
    page.padding = 0
    page.window_width = 400
    page.window_height = 850
    page.bgcolor = ft.colors.BLUE_100
    page.window_resizable = False
    page.window_maximizable = False
    page.theme_mode = ft.ThemeMode.LIGHT

    def show_exit_dialog(e):
        """function that is called, when user has clicked on
           exit button or red cross in top left corner of window"""
        if e.data == "close":
            dialogs.show_confirm_exit_dialog(page)

    page.window_prevent_close = True
    page.on_window_event = show_exit_dialog

    def views(_):
        """routing"""
        views_list = [home_r.create_home_view(page)]
        if page.route == "/new" or page.route == "/statistics":
            views_list.append(new_entry_r.create_new_entry_view(page))
        if page.route == "/statistics":
            views_list.append(statistics_r.create_statistics_view(page))
        page.views[:] = views_list
        page.update()

    def view_pop(_):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = views
    page.on_view_pop = view_pop
    page.go(page.route)


# START OF THE APP
ft.app(target=main)
