import openpyxl
import flet as ft
from datetime import datetime, timedelta
import re

pattern = r'(\d+:\d+)'


# FUNCTIONS THAT WORKS WITH EXCEL


def data_for_table():
    file_fill = "walking_data.xlsx"
    wb = openpyxl.load_workbook(file_fill, data_only=True)
    ws = wb['Sheet1']

    data = []
    for num in reversed(range(ws.max_row - 3, ws.max_row + 1)):
        date = ws[f'a{num}'].value if type(ws[f'a{num}'].value) is str else ws[f'a{num}'].value.strftime('%d/%m/%Y')
        kms = ws[f'b{num}'].value
        data.append((date, kms))

    wb.close()
    return data


def save_to_excel(date, kms: float, time, kcal: int, steps: int):
    file_save = "walking_data.xlsx"
    wb = openpyxl.load_workbook(file_save)
    ws = wb['Sheet1']
    insert_into_excel = [date,
                         kms,
                         time,
                         kcal,
                         steps]
    ws.append(insert_into_excel)
    wb.save("walking_data.xlsx")
    wb.close()


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

    #  FUNCTION BODY OF THE APP

    def window_event(e):
        if e.data == "close" or e.name == "click":
            page.dialog = confirm_dialog
            confirm_dialog.open = True
            page.update()

    page.window_prevent_close = True
    page.on_window_event = window_event

    def open_statistics(e):
        page.go("/statistics")

    def yes_click(e):
        page.window_destroy()

    def no_click(e):
        confirm_dialog.open = False
        page.update()

    def return_back(e):
        incomplete_dialog.open = False
        page.update()

    def success(e):
        success_dialog.open = False
        fill_table()
        page.update()

    def go_pick_date(e):
        no_date_picked_dialog.open = False
        page.update()

    def fill_table():
        data_table.rows = []
        data_table.rows = [
            ft.DataRow(
                [ft.DataCell(ft.Text(date)), ft.DataCell(ft.Text(kms))]
            ) for date, kms in data_for_table()
        ]
        page.update()

    def statistics(e):
        file_st = "walking_data.xlsx"
        workbook = openpyxl.load_workbook(file_st, data_only=True)
        worksheet = workbook['Sheet1']
        column_km = worksheet["B"]
        column_kcal = worksheet["D"]
        column_steps = worksheet["E"]
        total_km, total_kcal, total_steps = 0, 0, 0
        total_time = timedelta()

        for cell in column_km:
            if isinstance(cell.value, (int, float)):
                total_km += float(cell.value)

        for row in worksheet.iter_rows(min_row=4, max_col=3, values_only=True):
            time = datetime.strptime(str(row[2]), "%H:%M:%S").time()
            time_timedelta = timedelta(
                hours=time.hour,
                minutes=time.minute,
                seconds=time.second
            )
            total_time += time_timedelta

        for cell in column_kcal:
            if isinstance(cell.value, (int, float)):
                total_kcal += int(cell.value)

        for cell in column_steps:
            if isinstance(cell.value, (int, float)):
                total_steps += int(cell.value)

        workbook.close()
        return total_km, total_time, total_kcal, total_steps

    def pick_date(e):
        picked_date.value = "Budeš přidávat aktivitu ze dne {}".format(date_picker.value.strftime("%d/%m/%y"))
        page.update()

    def open_google_maps(e):
        page.launch_url("https://mapy.cz/")

    def save_time_entry(walked_time_entry_value):
        if re.search(pattern, walked_time_entry_value):
            time_format_save = f"{walked_time_entry_value}:00"
            return time_format_save
        else:
            time_format_save = f"{walked_time_entry_value}:00:00"
            return time_format_save

    def save_clicked(e):
        try:
            if not all([walked_time_entry.value, walked_kms_entry.value, walked_kcal_entry.value,
                        walked_steps_entry.value]):
                raise ValueError
            if not date_picker.value:
                raise AttributeError

        except ValueError:
            page.dialog = incomplete_dialog
            incomplete_dialog.open = True
            page.update()

        except AttributeError:
            page.dialog = no_date_picked_dialog
            no_date_picked_dialog.open = True
            page.update()
            page.go("/")

        else:
            date = date_picker.value.strftime("%d/%m/%y")
            kms = float(walked_kms_entry.value)
            time = save_time_entry(walked_time_entry.value)
            kcal = int(walked_kcal_entry.value)
            steps = int(walked_steps_entry.value)

            save_to_excel(date, kms, time, kcal, steps)

            page.dialog = success_dialog
            success_dialog.open = True

            walked_kms_entry.value = ""
            walked_time_entry.value = ""
            walked_kcal_entry.value = ""
            walked_steps_entry.value = ""
            page.update()

    # CONTROLS OF THE APP - DIALOGUES, BUTTONS, TEXTS

    welcome_txt = ft.Text(value="\nVítej ve WalkingApp!\n",
                          color=ft.colors.INDIGO,
                          style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                          text_align=ft.TextAlign.CENTER)

    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Potvrzení"),
        content=ft.Text("Opravdu si přeješ apku ukončit?"),
        actions=[
            ft.ElevatedButton("Ano", on_click=yes_click),
            ft.ElevatedButton("Ne", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    incomplete_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Něco jsi zapomněl"),
        content=ft.Text("Vše musí být vyplněno"),
        actions=[
            ft.ElevatedButton("OK, doplním", on_click=return_back)
        ])

    no_date_picked_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Chybí vybrané datum"),
        content=ft.Text("Vyber datum prosím"),
        actions=[
            ft.ElevatedButton("Jdu vybrat", on_click=go_pick_date)
        ])

    success_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Úspěch"),
        content=ft.Text("Vše bylo úspěšně zapsáno"),
        actions=[
            ft.ElevatedButton("OK", on_click=success)
        ])

    walked_kms_entry = ft.TextField(label="Kolik jsi ušel?",
                                    hint_text="km.m",
                                    width=160,
                                    border_radius=0,
                                    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9.]",
                                                                replacement_string=""),
                                    keyboard_type=ft.KeyboardType.NUMBER)
    walked_time_entry = ft.TextField(label="Za jak dlouho?",
                                     hint_text="hodiny:minuty",
                                     width=160,
                                     border_radius=0,
                                     input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9:]",
                                                                 replacement_string=""))
    walked_kcal_entry = ft.TextField(label="Kolik kalorií?",
                                     width=160,
                                     border_radius=0,
                                     input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]",
                                                                 replacement_string=""),
                                     keyboard_type=ft.KeyboardType.NUMBER)
    walked_steps_entry = ft.TextField(label="A kolik kroků?",
                                      width=160,
                                      border_radius=0,
                                      input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]",
                                                                  replacement_string=""),
                                      keyboard_type=ft.KeyboardType.NUMBER)

    date_picker = ft.DatePicker(on_change=pick_date,
                                first_date=datetime(2023, 10, 1),
                                last_date=datetime(2030, 12, 31)
                                )

    date_button = ft.ElevatedButton("Vyber datum",
                                    icon=ft.icons.CALENDAR_MONTH_ROUNDED,
                                    on_click=lambda _: date_picker.pick_date(),
                                    )
    picked_date = ft.Text(value="Vyber datum",
                          text_align=ft.TextAlign.CENTER,
                          color=ft.colors.WHITE54)

    data_table = ft.DataTable(
        bgcolor=ft.colors.WHITE54,
        columns=[
            ft.DataColumn(ft.Text("Datum")),
            ft.DataColumn(ft.Text("Kilometry")),
        ],
        rows=[]
    )

    fill_table()
    page.overlay.append(date_picker)

    open_maps = ft.Chip(
        label=ft.Text("Nápad na trasu"),
        leading=ft.Icon(ft.icons.MAP_SHARP),
        on_click=open_google_maps,
    )

    # GUI OF THE APP

    def views(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                bgcolor=ft.colors.BLUE_100,
                padding=0,
                controls=[ft.Stack(
                    [
                        ft.Image(
                            src="https://picsum.photos/id/651/400/800",
                            width=page.window_width,
                            height=page.window_height,
                            fit=ft.ImageFit.FILL
                        ),
                        ft.Container(left=65,
                                     height=200,
                                     width=270,
                                     content=welcome_txt),
                        ft.Container(right=100,
                                     top=280,
                                     width=180,
                                     height=35,
                                     content=date_button),
                        ft.Container(right=90,
                                     top=325,
                                     height=50,
                                     width=200,
                                     content=picked_date),
                        ft.Container(right=90,
                                     top=420,
                                     width=200,
                                     height=30,
                                     content=ft.FilledButton("Přidej nový záznam", on_click=lambda _:
                                     page.go("/new"))),
                        ft.Container(right=90,
                                     bottom=195,
                                     width=200,
                                     height=50,
                                     content=open_maps),
                        ft.Container(right=5,
                                     bottom=80,
                                     width=100,
                                     height=25,
                                     content=ft.ElevatedButton("Konec",
                                                               style=ft.ButtonStyle(
                                                                   shape=ft.ContinuousRectangleBorder(radius=30)),
                                                               on_click=window_event)),
                    ],
                    width=page.window_width,
                    height=page.window_height)],
            )
        )
        if page.route == "/new" or page.route == "/statistics":
            page.views.append(
                ft.View(
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
                            ft.Container(content=walked_kms_entry,
                                         top=30,
                                         left=25,
                                         bgcolor=ft.colors.BLUE_50),
                            ft.Container(content=walked_time_entry,
                                         top=30,
                                         left=200,
                                         bgcolor=ft.colors.BLUE_50),
                            ft.Container(content=walked_kcal_entry,
                                         top=110,
                                         left=25,
                                         bgcolor=ft.colors.BLUE_50),
                            ft.Container(content=walked_steps_entry,
                                         top=110,
                                         left=200,
                                         bgcolor=ft.colors.BLUE_50),
                            ft.Container(content=ft.ElevatedButton(text="Uložit", on_click=save_clicked),
                                         top=200,
                                         left=20),
                            ft.Container(content=ft.ElevatedButton("Ukaž statistiky", on_click=open_statistics),
                                         left=20,
                                         top=250),
                            ft.Container(content=data_table,
                                         left=70,
                                         top=350),
                            ft.Container(content=ft.ElevatedButton("Konec",
                                                                   style=ft.ButtonStyle(
                                                                       shape=ft.ContinuousRectangleBorder(radius=30)),
                                                                   on_click=window_event),
                                         right=5,
                                         bottom=80,
                                         width=100,
                                         height=25),

                        ],
                            width=page.window_width,
                            height=page.window_height - 70)]
                )
            )

        if page.route == "/statistics":
            page.views.append(
                ft.View(
                    "/statistics",
                    bgcolor=ft.colors.BLUE_100,
                    appbar=ft.AppBar(title=ft.Text("Statistiky"),
                                     bgcolor=ft.colors.BLUE_100),
                    padding=0,
                    controls=[
                        ft.Stack(controls=[
                            ft.Image(
                                src="https://picsum.photos/id/651/400/800",
                                width=page.window_width,
                                height=page.window_height,
                                fit=ft.ImageFit.FILL),
                            ft.Container(content=ft.Text("{} Km".format(round(statistics("e")[0], 2))),
                                         margin=10,
                                         padding=10,
                                         alignment=ft.alignment.center,
                                         bgcolor=ft.colors.AMBER,
                                         border_radius=90,
                                         width=175,
                                         height=100,
                                         left=100,
                                         top=20),
                            ft.Container(content=ft.Text("{} hod.".format(statistics("e")[1])),
                                         margin=10,
                                         padding=10,
                                         alignment=ft.alignment.center,
                                         bgcolor=ft.colors.GREEN_200,
                                         border_radius=90,
                                         width=175,
                                         height=100,
                                         left=100,
                                         top=150),
                            ft.Container(content=ft.Text("{} Kcal".format(statistics("e")[2])),
                                         margin=10,
                                         padding=10,
                                         alignment=ft.alignment.center,
                                         bgcolor=ft.colors.CYAN_200,
                                         border_radius=90,
                                         width=175,
                                         height=100,
                                         left=100,
                                         top=280),
                            ft.Container(content=ft.Text("{} kroků".format(statistics("e")[3])),
                                         margin=10,
                                         padding=10,
                                         alignment=ft.alignment.center,
                                         bgcolor=ft.colors.RED_200,
                                         border_radius=90,
                                         width=175,
                                         height=100,
                                         left=100,
                                         top=410),
                            ft.Container(content=ft.ElevatedButton("Konec",
                                                                   style=ft.ButtonStyle(
                                                                       shape=ft.ContinuousRectangleBorder(radius=30)),
                                                                   on_click=window_event),
                                         right=5,
                                         bottom=80,
                                         width=100,
                                         height=25),
                        ],
                            width=page.window_width,
                            height=page.window_height - 70)]
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = views
    page.on_view_pop = view_pop
    page.go(page.route)


# START OF THE APP

ft.app(target=main)
