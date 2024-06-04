import flet as ft


def main(page):
    page.title = 'Cartão'
    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),
                            title=ft.Text('Cartão pricipal'),
                            subtitle=ft.Text('Card subtitulo'),
                        ),
                        ft.Row(
                            [
                                ft.TextButton('texto com botão'),
                                ft.TextButton('texto com botão 2'),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    )


ft.app(target=main)
