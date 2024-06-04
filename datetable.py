import flet as ft


def main(page: ft.Page):
    page.title = 'Tabela em flet'
    page.window_width = 800
    page.window_height = 600
    page.bgcolor = 'green'
    page.add(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text('Primiero nome')),
                ft.DataColumn(ft.Text('Último nome')),
                ft.DataColumn(ft.Text('Idade')),
            ],
            bgcolor='black',
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text('João')),
                        ft.DataCell(ft.Text('Silva')),
                        ft.DataCell(ft.Text('33')),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text('João')),
                        ft.DataCell(ft.Text('Vitor')),
                        ft.DataCell(ft.Text('32')),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text('João')),
                        ft.DataCell(ft.Text('Manoel')),
                        ft.DataCell(ft.Text('35')),
                    ],
                ),
            ],
        )
    )


ft.app(target=main)
