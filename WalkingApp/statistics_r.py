import flet as ft
import excel_func
import home_r


def route_statistics(page, func_exit):
    total_km, total_time, total_kcal, total_steps = excel_func.statistics()
    view_statistics = ft.View(
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
                                ft.Container(content=ft.Text("{} Km".format(round(total_km))),
                                             margin=10,
                                             padding=10,
                                             alignment=ft.alignment.center,
                                             bgcolor=ft.colors.AMBER,
                                             border_radius=90,
                                             width=175,
                                             height=100,
                                             left=100,
                                             top=20),
                                ft.Container(content=ft.Text("{} hod.".format(total_time)),
                                             margin=10,
                                             padding=10,
                                             alignment=ft.alignment.center,
                                             bgcolor=ft.colors.GREEN_200,
                                             border_radius=90,
                                             width=175,
                                             height=100,
                                             left=100,
                                             top=150),
                                ft.Container(content=ft.Text("{} Kcal".format(total_kcal)),
                                             margin=10,
                                             padding=10,
                                             alignment=ft.alignment.center,
                                             bgcolor=ft.colors.CYAN_200,
                                             border_radius=90,
                                             width=175,
                                             height=100,
                                             left=100,
                                             top=280),
                                ft.Container(content=ft.Text("{} kroků".format(total_steps)),
                                             margin=10,
                                             padding=10,
                                             alignment=ft.alignment.center,
                                             bgcolor=ft.colors.RED_200,
                                             border_radius=90,
                                             width=175,
                                             height=100,
                                             left=100,
                                             top=410),
                                ft.Container(content=home_r.exit_button_create(func_exit),
                                             right=5,
                                             bottom=80,
                                             width=100,
                                             height=25),
                            ],
                                width=page.window_width,
                                height=page.window_height - 70)]
                    )
    return view_statistics
