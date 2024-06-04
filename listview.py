import flet as ft


def main(page: ft.Page):
    page.title = "ListView"
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

    # criando coluna
    coluna = ft.Column(spacing=5, controls=item)

    # criando ListView
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
    lv.controls.append(ft.Text('Colunas'))
    lv.controls.append(coluna)

    # criando GridView
    gv = ft.GridView(expand=1, runs_count=5, max_extent=150,
                     child_aspect_ratio=1.0, spacing=5, run_spacing=5)
    gv.controls.append(coluna)

    # inserindo row e coluna
    page.add(lv, gv)


ft.app(target=main)
