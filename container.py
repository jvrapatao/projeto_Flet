import flet as ft


def main(page: ft.Page):
    page.title = "Containers"
    page.padding = 0
    page.window_width = 400
    page.window_height = 550
    page.update()

    c1 = ft.Container(
        content=ft.ElevatedButton('Botão elevado no container 1'),
        bgcolor='red',
        padding=10,
    )

    c2 = ft.Container(
        content=ft.ElevatedButton('Botão elevado no container 2'),
        bgcolor='blue',
        padding=10,
    )

    c3 = ft.Container(
        content=ft.ElevatedButton('Botão elevado no container 3'),
        bgcolor='yellow',
        padding=10,
    )

    # inserindo container
    page.add(c1, c2, c3)


ft.app(target=main)
