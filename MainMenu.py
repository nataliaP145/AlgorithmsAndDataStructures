from logging import log

import flet as ft
from RBT_screen_practice import rbt_view_practice

ALGORITHMS_INFO = {
    "Red Black Tree": {
        "description": "A Red-Black Tree is a self-balancing binary search tree where each node has an extra bit for denoting the color of the node, either red or black. It ensures that the tree remains balanced during insertions and deletions.",
        "complexity": {
            "search": "O(log n)",
            "insert": "O(log n)",
            "delete": "O(log n)",
            "build": "O(n log n)"
        }
    },
    "opt 2": {
        "description": "dsc for opt 2"
    }
}


def main(page: ft.Page):
    page.title = "Algorithm and Data Structure"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 800
    page.window_height = 1200

    title_text = ft.Text(
        "Welcome to Algorithm and Data Structure Game",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE
    )

    subtitle_text = ft.Text(
        "Select an option below to explore different algorithms and data structures.",
        size=16,
        color=ft.Colors.WHITE
    )


    # algorithms_dropdown = ft.Dropdown(
    #    width=300,
    #     label="Select an Algorithm",
    #     value="Red Black Tree",
    #     options=[
    #         ft.dropdown.Option("Red Black Tree"),
    #         ft.dropdown.Option("opt 2"),
    #         ft.dropdown.Option("opt 3"),
    #         ft.dropdown.Option("opt 4"),
    #     ],
    # )

    def on_dropdown_select(e):
        print(f"Chosen algorithm: {algorithms_dropdown.value}")

    algorithms_dropdown = ft.Dropdown(
        width=300,
        label="Select an Algorithm",
        on_select=on_dropdown_select,
        options=[
            ft.DropdownOption(
                key="Red Black Tree",
                content=ft.Row(
                    controls=[
                        ft.Text("Red", color=ft.Colors.RED, weight=ft.FontWeight.BOLD),
                        ft.Text("Black", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                        ft.Text("Tree", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                    ],
                    tight=True
                )
            ),
            ft.DropdownOption("opt 2"),
            ft.DropdownOption("opt 3"),
            ft.DropdownOption("opt 4"),
        ],
    )

    def show_algorithm_info(e):
        selected = algorithms_dropdown.value
        info_text = ALGORITHMS_INFO.get(selected, {}).get("description", "No description available.")

        info_dialog = ft.AlertDialog(
            title=ft.Text(f"{selected} Information"),
            content=ft.Text(info_text),
            actions=[ft.TextButton(content=ft.Text("Close"), on_click=lambda e: close_dialog(info_dialog))]
        )

        page.overlay.append(info_dialog)
        info_dialog.open = True
        page.update()

    info_button = ft.IconButton(
        icon=ft.icons.INFO_OUTLINE,
        icon_color=ft.Colors.WHITE,
        tooltip="Show Algorithm Instruction",
        on_click=show_algorithm_info
    )

    mode_radio = ft.RadioGroup(
        content=ft.Row(
            controls=[
                ft.Radio(value="practice", label="Practice Mode (Training)"),
                ft.Radio(value="ranked", label="Ranked Mode (Points)"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=30
        ),
        value="practice" 
    )

    hints_switch = ft.Switch(
        label="Show Hints",
        value=False,
        on_change=lambda e: print("Hints switched to:", e.control.value)
    )



    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(ft.View("/", [card_menu], horizontal_alignment=ft.CrossAxisAlignment.CENTER, vertical_alignment=ft.MainAxisAlignment.CENTER))
        elif page.route == "/rbt_practice":
            page.views.append(
                ft.View(
                    "/rbt_practice",
                    [rbt_view_practice(page, algorithms_dropdown.value, mode_radio.value, hints_switch.value)],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER
                )
            )
        page.update()
    page.on_route_change = route_change

    def start_game(e):
        selected_algorithm = algorithms_dropdown.value
        show_hints = hints_switch.value
        if selected_algorithm == "Red Black Tree":
            page.go("/rbt_practice")
        else:
            print("Selected algorithm is not implemented yet.")

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
                ft.Text("Select Game Mode:", size=16, weight=ft.FontWeight.W_500, color=ft.Colors.WHITE),
                show_algorithm_info,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                info_button,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                mode_radio,
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