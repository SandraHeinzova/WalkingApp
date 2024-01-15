import flet as ft
import re
import dialogs
import excel_func
import statistics_r
import new_r
import controls
import home_r

pattern_hours_minutes = r'^([0-9]|1[0-2]|2[0-3]):[0-5][0-9]$'
pattern_hours = r'^(1?[0-9]|2[0-3])$'


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

    def open_statistics(_):
        page.go("/statistics")

    def save_time_entry(walked_time_entry_value):
        if re.search(pattern_hours_minutes, walked_time_entry_value):
            time_format_to_save = f"{walked_time_entry_value}:00"
            return time_format_to_save
        elif re.search(pattern_hours, walked_time_entry_value):
            time_format_to_save = f"{walked_time_entry_value}:00:00"
            return time_format_to_save
        else:
            dialogs.show_wrong_time_dialog(page)
            return None

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
        time = save_time_entry(new_r.walked_time_entry.value)
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
            page.views.append(new_r.route_new(page, save_clicked, open_statistics, window_event))
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
