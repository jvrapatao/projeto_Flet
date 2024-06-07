import flet as ft


def main(page: ft.Page):
    # configurações da pagina
    page.title = 'Lista de tarefas'
    page.window_width = 500
    page.window_height = 500

    # funcao para fechar o banner
    def close_banner(e):
        page.banner.open = False
        page.update()

    # configuracao do banner
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED,
                        color=ft.colors.AMBER, size=40),
        content=ft.Text('Ops, prencha todos os campos', color='black'),
        actions=[
            ft.TextButton('ok', on_click=close_banner),
        ],
    )

    # funcao inserir tarefa
    def inserir_tarefa(e):
        if caixa_texto.value == '':
            # mostrar notificacao de erro
            page.banner.open = True
            page.update()
        else:
            page.add(ft.Checkbox(label=caixa_texto.value))
            caixa_texto.value = ''
            caixa_texto.focus()
            caixa_texto.upadate()
    # caixa onde a tarefa será digitada
    caixa_texto = ft.TextField(
        hint_text='informe a tarefa a ser realizada', width=300, bgcolor='blue')
    # botão para inserir as tarefas a serem realizadas
    botao_adicionar = ft.ElevatedButton(
        'Incluir tarefa', bgcolor='green', on_click=inserir_tarefa)

    page.add(ft.Row([caixa_texto, botao_adicionar]))


ft.app(target=main)
