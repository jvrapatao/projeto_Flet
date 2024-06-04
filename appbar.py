import flet as ft


def main(page: ft.Page):
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text('AppBar'),
        center_title=False,
        bgcolor='GREEN',
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
        ],

    )
    page.update()


ft.app(target=main)
