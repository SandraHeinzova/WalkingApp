import flet as ft
import model
import dialogs


def create_statistics_view(page):
    """route to '/statistics'
    :param page: container for controls in View"""
    # button that exits application
    exit_button = ft.ElevatedButton(text="Konec",
                                    style=ft.ButtonStyle(
                                        shape=ft.ContinuousRectangleBorder(radius=30)),
                                    on_click=lambda e: dialogs.show_confirm_exit_dialog(e.page))

    total_km, total_time, total_kcal, total_steps = model.calculate_statistics()
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
                ft.Container(content=ft.Text("{} Km".format(round(total_km) if total_km else 0)),
                             margin=10,
                             padding=10,
                             alignment=ft.alignment.center,
                             bgcolor=ft.colors.AMBER,
                             border_radius=90,
                             width=175,
                             height=100,
                             left=100,
                             top=20),
                ft.Container(content=ft.Text("{} hod.".format(total_time if total_time else "0")),
                             margin=10,
                             padding=10,
                             alignment=ft.alignment.center,
                             bgcolor=ft.colors.GREEN_200,
                             border_radius=90,
                             width=175,
                             height=100,
                             left=100,
                             top=150),
                ft.Container(content=ft.Text("{} Kcal".format(total_kcal if total_kcal else "0")),
                             margin=10,
                             padding=10,
                             alignment=ft.alignment.center,
                             bgcolor=ft.colors.CYAN_200,
                             border_radius=90,
                             width=175,
                             height=100,
                             left=100,
                             top=280),
                ft.Container(content=ft.Text("{} kroků".format(total_steps if total_steps else "0")),
                             margin=10,
                             padding=10,
                             alignment=ft.alignment.center,
                             bgcolor=ft.colors.RED_200,
                             border_radius=90,
                             width=175,
                             height=100,
                             left=100,
                             top=410),
                ft.Container(content=exit_button,
                             right=5,
                             bottom=80,
                             width=100,
                             height=25),
            ],
                width=page.window_width,
                height=page.window_height - 70)]
    )

    return view_statistics
