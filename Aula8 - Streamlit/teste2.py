import flet as ft

def main(page: ft.Page):
    # Configuração da página
    page.title = "Lista de Tarefas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.ADAPTIVE
    
    # Lista para armazenar as tarefas
    tarefas = []
    
    # Função para adicionar nova tarefa
    def adicionar_tarefa(e):
        if entrada_tarefa.value.strip():  # Verifica se não está vazio
            # Cria um container para a tarefa com layout em linha
            tarefa_container = ft.Container(
                content=ft.Row([
                    ft.Checkbox(
                        value=False,
                        on_change=lambda e, t=entrada_tarefa.value: marcar_concluida(e, t)
                    ),
                    ft.Text(
                        entrada_tarefa.value,
                        size=16,
                        expand=True
                    ),
                    ft.IconButton(
                        icon=ft.icons.DELETE_OUTLINE,
                        icon_color=ft.colors.RED_400,
                        tooltip="Remover tarefa",
                        on_click=lambda e, t=entrada_tarefa.value: remover_tarefa(e, t)
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=10,
                bgcolor=ft.colors.WHITE,
                border_radius=8,
                border=ft.border.all(1, ft.colors.GREY_300),
                margin=ft.margin.only(bottom=5)
            )
            
            # Adiciona à lista de tarefas e à lista visual
            tarefas.append(tarefa_container)
            lista_tarefas.controls.append(tarefa_container)
            
            # Limpa o campo de entrada
            entrada_tarefa.value = ""
            
            # Atualiza a página
            page.update()
    
    # Função para marcar tarefa como concluída
    def marcar_concluida(e, tarefa_texto):
        if e.control.value:  # Se foi marcado
            e.control.parent.controls[1].style = ft.TextStyle(
                decoration=ft.TextDecoration.LINE_THROUGH,
                color=ft.colors.GREY_500
            )
        else:  # Se foi desmarcado
            e.control.parent.controls[1].style = None
        page.update()
    
    # Função para remover tarefa
    def remover_tarefa(e, tarefa_texto):
        for i, tarefa in enumerate(tarefas):
            if tarefa.content.controls[1].value == tarefa_texto:
                lista_tarefas.controls.remove(tarefa)
                tarefas.pop(i)
                break
        page.update()
    
    # Campo de entrada de texto
    entrada_tarefa = ft.TextField(
        hint_text="Digite uma nova tarefa...",
        border_radius=8,
        expand=True,
        on_submit=adicionar_tarefa,  # Permite adicionar com Enter
        autofocus=True
    )
    
    # Botão para adicionar tarefa
    botao_adicionar = ft.ElevatedButton(
        text="Adicionar",
        icon=ft.icons.ADD,
        on_click=adicionar_tarefa,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_600,
            padding=15
        )
    )
    
    # Container para a lista de tarefas
    lista_tarefas = ft.Column(
        spacing=5,
        scroll=ft.ScrollMode.ADAPTIVE
    )
    
    # Cabeçalho com contador de tarefas
    contador_tarefas = ft.Text("0 tarefas", size=14, color=ft.colors.GREY_600)
    
    def atualizar_contador(e):
        contador_tarefas.value = f"{len(tarefas)} tarefas"
        page.update()
    
    # Layout principal
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("📝 Minha Lista de Tarefas", 
                           size=24, 
                           weight=ft.FontWeight.BOLD,
                           color=ft.colors.BLUE_700)
                ], alignment=ft.MainAxisAlignment.CENTER),
                
                ft.Divider(height=20),
                
                # Área de entrada
                ft.Container(
                    content=ft.Row([
                        entrada_tarefa,
                        botao_adicionar
                    ]),
                    padding=10,
                    bgcolor=ft.colors.GREY_100,
                    border_radius=8
                ),
                
                ft.Divider(height=10),
                
                # Cabeçalho da lista
                ft.Row([
                    ft.Text("📋 Tarefas:", size=18, weight=ft.FontWeight.BOLD),
                    contador_tarefas
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                
                # Lista de tarefas
                ft.Container(
                    content=lista_tarefas,
                    padding=10,
                    bgcolor=ft.colors.GREY_50,
                    border_radius=8,
                    height=400
                )
            ]),
            width=600,
            padding=20,
            border_radius=12,
            bgcolor=ft.colors.WHITE,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.colors.GREY_300
            )
        )
    )
    
    # Atualiza contador quando tarefas mudam
    def on_tarefa_adicionada(e):
        contador_tarefas.value = f"{len(tarefas)} tarefas"
        page.update()
    
    # Modifica a função adicionar_tarefa para também atualizar o contador
    original_adicionar = adicionar_tarefa
    def novo_adicionar(e):
        original_adicionar(e)
        on_tarefa_adicionada(e)
    adicionar_tarefa = novo_adicionar

ft.app(target=main)