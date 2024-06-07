import flet as ft


def main(page: ft.Page):
    page.window_width = 900
    page.window_height = 600
    page.bgcolor = 'blue'
    
    t = ft.Text(value='Controles de texto Label',
                bgcolor='white', color='black')
    page.add(t)
    # t.value = 'equivale ao método Text() => controles de texto Label'
    # page.update()


    a = ft.Text('A', bgcolor='red', color='black')
    b = ft.Text('B')
    c = ft.Text('C')
    page.add(ft.Row(controls=[a, b, c]))
    # page.add(
    #     ft.Row(
    #         controls=[
    #             ft.Text('A'),
    #             ft.Text('B'),
    #             ft.Text('C'),
    #         ]
    #     )
    # )


ft.app(target=main)
