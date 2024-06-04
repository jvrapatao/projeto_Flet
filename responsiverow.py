import flet as ft


def main(page: ft.Page):
    # res = ft.ResponsiveRow(
    #     ft.Column(col={'small': 6}, controls=[ft.Text('Coluna 1')]),
    #     ft.Column(col={'small': 6}, controls=[ft.Text('Coluna 2')]),
    # )

    #pw = ft.Text(bottom=50, width=50, style='displaysmall')
    #page.overlay.append(pw)

    page.add(
        ft.ResponsiveRow(
            [
                ft.Container(
                    ft.Text('Coluna 1'),
                    padding=5,
                    bgcolor=ft.colors.GREEN,
                    col={'sm': 6, 'md': 4, 'xl': 2},
                ),
                ft.Container(
                    ft.Text('Coluna 2'),
                    padding=5,
                    bgcolor=ft.colors.GREY,
                    col={'sm': 6, 'md': 4, 'xl': 2},
                ),
                ft.Container(
                    ft.Text('Coluna 3'),
                    padding=5,
                    bgcolor=ft.colors.BLUE,
                    col={'sm': 6, 'md': 4, 'xl': 2},
                ),
                ft.Container(
                    ft.Text('Coluna 4'),
                    padding=5,
                    bgcolor=ft.colors.PINK,
                    col={'sm': 6, 'md': 4, 'xl': 2},
                ),
            ]
        )
    )


ft.app(target=main)
