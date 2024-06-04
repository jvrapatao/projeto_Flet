import flet as ft


def main(page: ft.Page):
    # adicionar controllers da página
    page.padding = 0
    page.window_width = 400
    page.window_height = 550
    # add()=> não é necessário usar o page.update()
    page.add(ft.Text('olá'))
    # page.controls.append(ft.Text('Olá'))
    # page.update()


ft.app(port=0000, target=main)
