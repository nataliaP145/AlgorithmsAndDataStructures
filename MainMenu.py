import flet as ft
import random

def main(page: ft.Page):
    page.title = "Main Menu - Algorithm and Data Structure"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 800
    page.window_height = 800

    title_text = ft.Text(
        "Welcome to the Main Menu",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE
    )

    subtitle_text = ft.Text(
        "Select an option below to explore different algorithms and data structures.",
        size=16,
        color=ft.Colors.WHITE
    )

    algorithms_dropdown = ft.Dropdown(
        width=300,
        label="Select an Algorithm",
        value="RBT",
        options=[
            ft.dropdown.Option("RBT"),
            ft.dropdown.Option("opt 2"),
            ft.dropdown.Option("opt 3"),
            ft.dropdown.Option("opt 4"),
        ],
    )

    hints_switch = ft.Switch(
        label="Show Hints",
        value=False,
        on_change=lambda e: print("Hints switched to:", e.control.value)
    )

    def start_game(e):
        selected_algorithm = algorithms_dropdown.value
        show_hints = hints_switch.value
        print(f"Starting game with {selected_algorithm}, Show Hints: {show_hints}")
        dialog = ft.AlertDialog(
            title=ft.Text("Game Started"),
            content=ft.Text(f"Algorithm: {selected_algorithm}\nShow Hints: {show_hints}"),
            actions=[ft.TextButton(content=ft.Text("OK"), on_click=lambda x: close_dialog(dialog))]
        )
        page.overlay.append(dialog)
        dialog.open = True
        page.update()

    def close_dialog(dialog):
        dialog.open = False
        page.update()

    start_button = ft.Button(
        content=ft.Text("Start Game"),
        icon=ft.Icons.PLAY_ARROW,
        style=ft.ButtonStyle(
            padding=ft.Padding(20, 10, 20, 10),
            shape=ft.RoundedRectangleBorder(radius=10)
        ),
        width=200,
        on_click=start_game
    )

    card_menu = ft.Container(
        content=ft.Column(
            [
                title_text,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                subtitle_text,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                algorithms_dropdown,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                hints_switch,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                start_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        padding=20,
        border_radius=10,
        border=ft.Border.all(1, ft.Colors.WHITE), 
        bgcolor=ft.Colors.BLUE_GREY_900,
    )

    page.add(card_menu)

ft.run(main)