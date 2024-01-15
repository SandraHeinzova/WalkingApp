import flet as ft
import controls


def route_new(page, func_save, func_stat, func_exit):
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
                            ft.Container(content=controls.walked_kms_entry,
                                         top=30,
                                         left=25,
                                         bgcolor=ft.colors.BLUE_50),
                            ft.Container(content=controls.walked_time_entry,
                                         top=30,
                                         left=200,
                                         bgcolor=ft.colors.BLUE_50),
                            ft.Container(content=controls.walked_kcal_entry,
                                         top=110,
                                         left=25,
                                         bgcolor=ft.colors.BLUE_50),
                            ft.Container(content=controls.walked_steps_entry,
                                         top=110,
                                         left=200,
                                         bgcolor=ft.colors.BLUE_50),
                            ft.Container(content=controls.save_button_create(func_save),
                                         top=200,
                                         left=20),
                            ft.Container(content=controls.show_stat_button_create(func_stat),
                                         left=20,
                                         top=250),
                            ft.Container(content=controls.data_table,
                                         left=70,
                                         top=350),
                            ft.Container(content=controls.exit_button_create(func_exit),
                                         right=5,
                                         bottom=80,
                                         width=100,
                                         height=25)
                        ],
                            width=page.window_width,
                            height=page.window_height - 70)]
                )

    return view_new
