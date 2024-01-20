import flet as ft
import dialogs
import statistics_r
import new_r
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

    def window_event(e):
        """function that is called, when user has clicked on
           exit button or red cross in top left corner of window"""
        if e.data == "close" or e.name == "click":
            dialogs.show_confirm_dialog(page)

    page.window_prevent_close = True
    page.on_window_event = window_event

    # adding date picker to the application
    page.overlay.append(home_r._date_picker)

    def views(_):
        """routing"""
        page.views.clear()
        page.views.append(home_r.route_home(page))
        if page.route == "/new" or page.route == "/statistics":
            page.views.append(new_r.route_new(page))
        if page.route == "/statistics":
            page.views.append(statistics_r.route_statistics(page))
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
