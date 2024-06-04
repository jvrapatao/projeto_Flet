import flet as ft


def main(page: ft.Page):
    page.title = "Containers"
    page.padding = 0
    page.window_width = 1000
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

    # criando lista
    item = [c1, c2, c3]

    # criando row
    row = ft.Row(spacing=10, controls=item)

    # criando coluna
    coluna = ft.Column(spacing=5, controls=item)

    # criando stack
    st = ft.Stack(
        [
            ft.ElevatedButton('Botão stack'),
        ],
        width=300,
        height=300
    )

    # inserindo row e coluna
    page.add(row, coluna, st)


ft.app(target=main)
