import flet as ft


def main(page: ft.Page):
    # largura e altura da pagina
    page.window_width = 400
    page.window_height = 550

    # configuracao da pagina
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.MULTILINE_CHART),
        leading_width=40,
        title=ft.Text('Calculadora IMC'),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT
    )

    # funcao para fechar o banner
    def close_banner(e):
        page.banner.open = False
        page.update()

    # configuracao do banner de notificacao
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED,
                        color=ft.colors.AMBER, size=40),
        content=ft.Text('Ops! preencha todos os campos'),
        actions=[ft.TextButton('OK', on_click=close_banner),],
    )

    def calcular(e):
        if peso.value == '' or altura.value == '' or genero.value == '':
            page.banner.open = True
            page.update()
        else:
            valor_peso = float(peso.value)
            valor_altura = float(altura.value)
            # calcular IMC
            imc = valor_peso/(valor_altura*valor_altura)
            imc = float(f'{imc:2f}')
            # exibir valor IMC
            IMC.value = f'Seu IMC é {imc}'

            if genero.value == 'Feminino':
                if imc < 18.5:
                    detalhes.value = 'Abaixo do peso'
                elif 18.5 <= imc < 24.9:
                    detalhes.value = 'Peso saudável'
                elif 25 <= imc < 29.9:
                    detalhes.value = 'Sobrepeso'
                elif 30 <= imc < 34.9:
                    detalhes.value = 'Obeso'
                else:
                    detalhes.value = 'Obeso severo'
            else:
                if imc < 18.5:
                    detalhes.value = 'Abaixo do peso'
                elif 18.5 <= imc < 24.9:
                    detalhes.value = 'Peso saudável'
                elif 25 <= imc < 29.9:
                    detalhes.value = 'Sobrepeso'
                elif 30 <= imc < 34.9:
                    detalhes.value = 'Obeso'
                else:
                    detalhes.value = 'Obeso severo'
            # limpar campos
            peso.value = ''
            altura.value = ''
            genero.value = ''
            # atualizar página
            page.update()

    # caixas de texto onde serão inseridas as informações
    altura = ft.TextField(
        label='Altura',
        hint_text='Informe sua altura',
        border_color=ft.colors.YELLOW_ACCENT)

    peso = ft.TextField(
        label='Peso',
        hint_text='Informe seu peso',
        border_color=ft.colors.YELLOW_ACCENT)

    genero = ft.Dropdown(
        label='Gênero',
        hint_text='Selecione seu gênero',
        border_color=ft.colors.YELLOW_ACCENT,
        options=[
            ft.dropdown.Option('Masculino'),
            ft.dropdown.Option('Feminino'),
        ]
    )
    
    # botão para calcular o IMC
    b_calcular = ft.ElevatedButton(
        text='Calcular IMC',
        color=ft.colors.YELLOW_ACCENT,
        on_click=calcular)

    # Informações do IMC
    IMC = ft.Text('Seu IMC é: ', size=30)
    detalhes = ft.Text('Informe seus dados abaixo', size=20)

    info_resultado_app = ft.Column(
        controls=[
            IMC,
            detalhes,
        ]
    )

    info = ft.Row(
        controls=[
            info_resultado_app,
        ]
    )

    # layout da pagina
    layout = ft.ResponsiveRow(
        [
            ft.Container(
                info,
                padding=5,
                col={'sm': 4, 'md': 4, 'xl': 4},
                alignment=ft.alignment.center,
            ),

            ft.Container(
                altura,
                padding=5,
                col={'sm': 12, 'md': 3, 'xl': 3},
            ),

            ft.Container(
                peso,
                padding=5,
                col={'sm': 12, 'md': 3, 'xl': 3},
            ),

            ft.Container(
                genero,
                padding=5,
                col={'sm': 12, 'md': 3, 'xl': 3},
            ),

            ft.Container(
                b_calcular,
                padding=5,
                col={'sm': 12, 'md': 3, 'xl': 3},
            ),
        ]
    )

    page.add(layout)


ft.app(target=main)
