import flet as ft
import dialogs
import excel_func
import statistics_r
import new_r
import controls
import home_r


# MAIN BODY OF THE APP WRAP IN FUNCTION MAIN
def main(page: ft.Page):
    page.title = "WalkingApp"
    page.padding = 0
    page.window_width = 400
    page.window_height = 850
    page.bgcolor = ft.colors.BLUE_100
    page.window_resizable = False
    page.window_maximizable = False
    page.theme_mode = ft.ThemeMode.LIGHT

    def window_event(e):
        if e.data == "close" or e.name == "click":
            dialogs.show_confirm_dialog(page)

    page.window_prevent_close = True
    page.on_window_event = window_event

    def save_clicked(_):
        if not all([new_r.walked_time_entry.value, new_r.walked_kms_entry.value, new_r.walked_kcal_entry.value,
                    new_r.walked_steps_entry.value]):
            dialogs.show_incomplete_dialog(page)
            return

        if not home_r.date_picker.value:
            page.go("/")
            dialogs.show_no_date_picked_dialog(page)
            return

        date = home_r.date_picker.value.strftime("%d/%m/%y")
        kms = float(new_r.walked_kms_entry.value)
        time = new_r.save_time_entry(page, new_r.walked_time_entry.value)
        kcal = int(new_r.walked_kcal_entry.value)
        steps = int(new_r.walked_steps_entry.value)

        if time is None:
            return

        excel_func.save_to_excel(date, kms, time, kcal, steps)

        dialogs.show_success_dialogue(page, controls.fill_recent_walks_table, new_r.data_table)

        new_r.walked_kms_entry.value = ""
        new_r.walked_time_entry.value = ""
        new_r.walked_kcal_entry.value = ""
        new_r.walked_steps_entry.value = ""
        page.update()

    controls.fill_recent_walks_table(page, new_r.data_table)
    page.overlay.append(home_r.date_picker)

    def views(_):
        page.views.clear()
        page.views.append(home_r.route_home(page, window_event))
        if page.route == "/new" or page.route == "/statistics":
            page.views.append(new_r.route_new(page, save_clicked, window_event))
        if page.route == "/statistics":
            page.views.append(statistics_r.route_statistics(page, window_event))
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
