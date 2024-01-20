import flet as ft
import re
import dialogs
import model

pattern_hours_minutes = r'^([0-9]|1[0-2]|2[0-3]):[0-5][0-9]$'
pattern_hours = r'^(1?[0-9]|2[0-3])$'


##################
# Event Handlers #
##################
def _exit_button_create():
    """creates a button that exits application"""
    exit_button = ft.ElevatedButton(text="Konec",
                                    style=ft.ButtonStyle(
                                        shape=ft.ContinuousRectangleBorder(radius=30)),
                                    on_click=lambda e: dialogs.show_confirm_dialog(e.page))
    return exit_button


def _open_statistics(e):
    """Redirects to the statistics page"""
    e.page.go("/statistics")


def _save_time_entry(page, walked_time_entry_value):
    """checks format of the entered time, returns time in format suitable for Excel
    :param page: container for controls in View
    :param walked_time_entry_value: value from walked_time_entry TextField"""
    if re.search(pattern_hours_minutes, walked_time_entry_value):
        time_format_to_save = f"{walked_time_entry_value}:00"
        return time_format_to_save
    elif re.search(pattern_hours, walked_time_entry_value):
        time_format_to_save = f"{walked_time_entry_value}:00:00"
        return time_format_to_save
    else:
        dialogs.show_wrong_time_dialog(page)
        return None


def _save_clicked(page):
    """starts after the save button is clicked, checks if all data are entered, transfers them into required formats
     and saves into Excel and the fields are cleared
     :param page: container for controls in View"""
    if not all([_walked_time_entry.value, _walked_kms_entry.value, _walked_kcal_entry.value,
                _walked_steps_entry.value]):
        dialogs.show_incomplete_dialog(page)
        return

    if not model.selected_date:
        page.go("/")
        dialogs.show_no_date_picked_dialog(page)
        return

    date = model.selected_date
    kms = float(_walked_kms_entry.value)
    time = _save_time_entry(page, _walked_time_entry.value)
    kcal = int(_walked_kcal_entry.value)
    steps = int(_walked_steps_entry.value)

    if time is None:
        return

    model.save_to_excel(date, kms, time, kcal, steps)

    dialogs.show_success_dialogue(page, _fill_recent_walks_table, _data_table)

    _walked_kms_entry.value = ""
    _walked_time_entry.value = ""
    _walked_kcal_entry.value = ""
    _walked_steps_entry.value = ""
    page.update()


def _save_button_create(page):
    """creates a saving button with on_click parameter and its function
    :param page: container for controls in View"""
    save_button = ft.ElevatedButton(text="Uložit",
                                    on_click=lambda _: _save_clicked(page))
    return save_button


def _fill_recent_walks_table(page, table):
    """gets data from Excel, goes through them and fills data table rows with date and kms values
    :param page: container for controls in View
    :param table: data_table"""
    walks_data = model.get_recent_walks()
    recent_walks = walks_data if walks_data else [("Žádné záznamy", "")]
    table.rows = [
        ft.DataRow(
            [ft.DataCell(ft.Text(date)), ft.DataCell(ft.Text(kms))]
        ) for date, kms in recent_walks]
    page.update()


###########
#  View   #
###########
# button for open the statistics page, on_click parameter with corresponding function
_show_statistics_button = ft.ElevatedButton(text="Ukaž statistiky",
                                            on_click=_open_statistics)

# data table that holds data from last four walks
_data_table = ft.DataTable(
    bgcolor=ft.colors.WHITE54,
    columns=[
        ft.DataColumn(ft.Text("Datum")),
        ft.DataColumn(ft.Text("Kilometry")),
    ],
    rows=[])

# field for walked kilometres
_walked_kms_entry = ft.TextField(label="Kolik jsi ušel?",
                                 hint_text="km.m",
                                 width=160,
                                 border_radius=0,
                                 input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9.]",
                                                             replacement_string=""),
                                 keyboard_type=ft.KeyboardType.NUMBER)

# field for time spent on walk
_walked_time_entry = ft.TextField(label="Za jak dlouho?",
                                  hint_text="hodiny:minuty",
                                  width=160,
                                  border_radius=0,
                                  input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9:]",
                                                              replacement_string=""))

# field for kcal burned on walk (according smartwatches etc.)
_walked_kcal_entry = ft.TextField(label="Kolik kalorií?",
                                  width=160,
                                  border_radius=0,
                                  input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]",
                                                              replacement_string=""),
                                  keyboard_type=ft.KeyboardType.NUMBER)
# field for number of steps made on walk (according smartwatches etc.)
_walked_steps_entry = ft.TextField(label="A kolik kroků?",
                                   width=160,
                                   border_radius=0,
                                   input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]",
                                                               replacement_string=""),
                                   keyboard_type=ft.KeyboardType.NUMBER)


###########
#  Route  #
###########
def routing_to_new(page):
    """route to '/new'
    :param page: container for controls in View"""
    # filling the data table with data from last four walks
    _fill_recent_walks_table(page, _data_table)
    view_new = ft.View(
        route="/new",
        bgcolor=ft.colors.BLUE_100,
        padding=0,
        appbar=ft.AppBar(title=ft.Text("Nový záznam"),
                         bgcolor=ft.colors.BLUE_100),
        controls=[
            ft.Stack(controls=[
                ft.Image(
                    src="https://picsum.photos/id/651/400/800",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.FILL),
                ft.Container(content=_walked_kms_entry,
                             top=30,
                             left=25,
                             bgcolor=ft.colors.BLUE_50),
                ft.Container(content=_walked_time_entry,
                             top=30,
                             left=200,
                             bgcolor=ft.colors.BLUE_50),
                ft.Container(content=_walked_kcal_entry,
                             top=110,
                             left=25,
                             bgcolor=ft.colors.BLUE_50),
                ft.Container(content=_walked_steps_entry,
                             top=110,
                             left=200,
                             bgcolor=ft.colors.BLUE_50),
                ft.Container(content=_save_button_create(page),
                             top=200,
                             left=20),
                ft.Container(content=_show_statistics_button,
                             left=20,
                             top=250),
                ft.Container(content=_data_table,
                             left=70,
                             top=350),
                ft.Container(content=_exit_button_create(),
                             right=5,
                             bottom=80,
                             width=100,
                             height=25)
            ],
                width=page.window_width,
                height=page.window_height - 70)]
    )

    return view_new
