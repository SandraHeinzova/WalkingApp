import flet as ft
import model
import dialogs


def create_statistics_view(page):
    """
    Return the view for the '/statistics' route.
    :param page: ft.Page
    """
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
                ft.Container(content=ft.Text(f"{round(total_km) if total_km else 0} Km"),
                             margin=10,
                             padding=10,
                             alignment=ft.alignment.center,
                             bgcolor=ft.colors.AMBER,
                             border_radius=90,
                             width=175,
                             height=100,
                             left=100,
                             top=20),
                ft.Container(content=ft.Text(f"{total_time // 60}:{total_time % 60:02}:00 hod." if total_time
                                             else "0 hod."),
                             margin=10,
                             padding=10,
                             alignment=ft.alignment.center,
                             bgcolor=ft.colors.GREEN_200,
                             border_radius=90,
                             width=175,
                             height=100,
                             left=100,
                             top=150),
                ft.Container(content=ft.Text(f"{total_kcal or 0} Kcal"),
                             margin=10,
                             padding=10,
                             alignment=ft.alignment.center,
                             bgcolor=ft.colors.CYAN_200,
                             border_radius=90,
                             width=175,
                             height=100,
                             left=100,
                             top=280),
                ft.Container(content=ft.Text(f"{total_steps or 0} kroků"),
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
