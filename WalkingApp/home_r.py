import flet as ft
import routing
import model

###########
#  View   #
###########
# textfield that shows welcome text
_welcome_txt = ft.Text(value="\nVítej ve WalkingApp!\n",
                       size=50,
                       color=ft.colors.CYAN_900,
                       theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM,
                       text_align=ft.TextAlign.CENTER)

# textfield that shows monthly statistics text
_monthly_stat_txt = ft.Text(value="\nTenhle měsíc:\n",
                            color=ft.colors.BLUE_GREY_50,
                            theme_style=ft.TextThemeStyle.DISPLAY_SMALL,
                            text_align=ft.TextAlign.CENTER)


# control that opens maps in the browser
_open_maps = ft.Chip(
    label=ft.Text("Nápad na trasu"),
    leading=ft.Icon(ft.icons.MAP_SHARP),
    on_click=lambda e: e.page.launch_url("https://mapy.cz/"),
)


###########
#  Route  #
###########
def create_home_view(page):
    """Return the view for the '/' route
    :param page: container for controls in View"""
    month_km, month_time, month_kcal, month_steps = model.calculate_monthly_statistics()
    view_home = ft.View(
        "/",
        bgcolor=ft.colors.BLUE_100,
        padding=0,
        navigation_bar=routing.nav_bar,
        controls=[ft.Stack(
            [
                ft.Image(
                    src="https://picsum.photos/id/651/400/800",
                    width=page.window_width,
                    height=page.window_height,
                    fit=ft.ImageFit.FILL
                ),
                ft.Container(left=55,
                             height=250,
                             width=300,
                             content=_welcome_txt),
                ft.Container(right=100,
                             top=280,
                             width=180,
                             height=35,
                             content=_open_maps),
                ft.Container(content=_monthly_stat_txt,
                             top=350,
                             left=90),
                ft.Container(content=ft.Text(f"{round(month_km) if month_km else 0} Km"),
                             top=450,
                             left=25,
                             margin=10,
                             padding=10,
                             alignment=ft.alignment.center,
                             border_radius=90,
                             width=150,
                             height=80,
                             bgcolor=ft.colors.BLUE_GREY_50),
                ft.Container(content=ft.Text(f"{month_time // 60}:{month_time % 60:02}:00 hod." if month_time
                                             else "0 hod."),
                             top=450,
                             left=200,
                             margin=10,
                             padding=10,
                             alignment=ft.alignment.center,
                             border_radius=90,
                             width=150,
                             height=80,
                             bgcolor=ft.colors.BLUE_GREY_50),
                ft.Container(content=ft.Text(f"{month_kcal or 0} Kcal"),
                             top=550,
                             left=25,
                             margin=10,
                             padding=10,
                             alignment=ft.alignment.center,
                             border_radius=90,
                             width=150,
                             height=80,
                             bgcolor=ft.colors.BLUE_GREY_50),
                ft.Container(content=ft.Text(f"{month_steps or 0} kroků"),
                             top=550,
                             left=200,
                             margin=10,
                             padding=10,
                             alignment=ft.alignment.center,
                             border_radius=90,
                             width=150,
                             height=80,
                             bgcolor=ft.colors.BLUE_GREY_50),
            ],
            width=page.window_width,
            height=page.window_height - 70)],
    )
    return view_home
