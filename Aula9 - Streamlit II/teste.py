import flet as ft

def main(page: ft.Page):
    # Configuração da página
    page.title = "Formulário de Contato"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Função para processar o envio do formulário
    def enviar_formulario(e):
        if nome_field.value and email_field.value and mensagem_field.value:
            print(f"Nome: {nome_field.value}")
            print(f"Email: {email_field.value}")
            print(f"Mensagem: {mensagem_field.value}")
            
            # Criar e mostrar a mensagem de confirmação
            page.overlay.append(
                ft.SnackBar(
                    content=ft.Text("Formulário enviado com sucesso!"),
                    bgcolor=ft.Colors.GREEN_400,
                    open=True,
                )
            )
            page.update()
        else:
            # Mensagem de erro se campos estiverem vazios
            page.overlay.append(
                ft.SnackBar(
                    content=ft.Text("Por favor, preencha todos os campos!"),
                    bgcolor=ft.Colors.RED_400,
                    open=True,
                )
            )
            page.update()
    
    # Campos do formulário
    nome_field = ft.TextField(
        label="Nome",
        hint_text="Digite seu nome completo",
        width=400,
    )
    
    email_field = ft.TextField(
        label="Email",
        hint_text="Digite seu email",
        width=400,
        keyboard_type=ft.KeyboardType.EMAIL,
    )
    
    mensagem_field = ft.TextField(
        label="Mensagem",
        hint_text="Digite sua mensagem",
        width=400,
        multiline=True,
        min_lines=3,
        max_lines=5,
    )
    
    # Botão de envio
    botao_enviar = ft.FilledButton(
        "Enviar Mensagem",
        on_click=enviar_formulario,
        width=400,
    )
    
    # Título
    titulo = ft.Text(
        "Formulário de Contato",
        size=32,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_700,
    )
    
    # Layout principal
    coluna = ft.Column(
        [
            titulo,
            ft.Divider(height=20, color=ft.Colors.BLUE_200),
            nome_field,
            ft.Container(height=10),
            email_field,
            ft.Container(height=10),
            mensagem_field,
            ft.Container(height=20),
            botao_enviar,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=5,
        width=500,
    )
    
    page.add(coluna)

# Executar a aplicação
if __name__ == "__main__":
    ft.run(main)