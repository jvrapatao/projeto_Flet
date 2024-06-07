import flet as ft


def main(page: ft.Page):
    page.title = 'Botão'
    page.window_width = 800
    page.window_height = 600
    page.bgcolor = 'white'

    def clique_botao(e):
        page.add(ft.Text(2+2))
        page.add(ft.Text('Clicado', color='black'))
        page.bgcolor ='red'

    bt = ft.ElevatedButton(text='Botão para clicar',
                           on_click=clique_botao)
    page.bgcolor ='black'
    page.add(bt)


ft.app(target=main)
