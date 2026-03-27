# hotel_system.py - Versão Final com Redirecionamento
import flet as ft
from datetime import datetime, date, timedelta
import uuid
from typing import List, Optional, Dict
import json

# ==================== CLASSES BASE ====================

class Pessoa:
    """Classe base para pessoas do sistema"""
    def __init__(self, nome: str, telefone: str, email: str):
        self._nome = nome
        self._telefone = telefone
        self._email = email
    
    # Getters e Setters com validação
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if not valor or len(valor.strip()) == 0:
            raise ValueError("Nome não pode estar vazio")
        self._nome = valor.strip()
    
    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, valor):
        if not valor or len(valor.strip()) == 0:
            raise ValueError("Telefone não pode estar vazio")
        self._telefone = valor.strip()
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        if '@' not in valor:
            raise ValueError("Email inválido")
        self._email = valor.strip()
    
    # Método polimórfico
    def exibir_informacoes(self) -> str:
        """Método base para exibir informações"""
        return f"Nome: {self._nome}\nTelefone: {self._telefone}\nEmail: {self._email}"


class Cliente(Pessoa):
    """Classe Cliente que herda de Pessoa"""
    def __init__(self, nome: str, telefone: str, email: str, cliente_id: str = None):
        super().__init__(nome, telefone, email)
        self.__id = cliente_id if cliente_id else str(uuid.uuid4())[:8]
    
    @property
    def id(self):
        return self.__id
    
    # Sobrescrita do método polimórfico
    def exibir_informacoes(self) -> str:
        return f"ID: {self.__id}\n{super().exibir_informacoes()}"
    
    def to_dict(self):
        return {
            'id': self.__id,
            'nome': self._nome,
            'telefone': self._telefone,
            'email': self._email
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['nome'], data['telefone'], data['email'], data['id'])


class Quarto:
    """Classe para gerenciar quartos"""
    def __init__(self, numero: int, tipo: str, preco_diaria: float):
        self.__numero = numero
        self.__tipo = tipo
        self.__preco_diaria = preco_diaria
        self.__disponivel = True
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def preco_diaria(self):
        return self.__preco_diaria
    
    @property
    def disponivel(self):
        return self.__disponivel
    
    def set_disponibilidade(self, status: bool):
        """Controla a disponibilidade do quarto"""
        self.__disponivel = status
    
    def exibir_informacoes(self) -> str:
        status = "Disponível" if self.__disponivel else "Ocupado"
        return f"Quarto {self.__numero} - {self.__tipo} - R$ {self.__preco_diaria:.2f}/diária - {status}"
    
    def to_dict(self):
        return {
            'numero': self.__numero,
            'tipo': self.__tipo,
            'preco_diaria': self.__preco_diaria,
            'disponivel': self.__disponivel
        }
    
    @classmethod
    def from_dict(cls, data):
        quarto = cls(data['numero'], data['tipo'], data['preco_diaria'])
        quarto.set_disponibilidade(data['disponivel'])
        return quarto


class Reserva:
    """Classe para gerenciar reservas"""
    def __init__(self, cliente: Cliente, quarto: Quarto, check_in: date, check_out: date):
        self.__cliente = cliente
        self.__quarto = quarto
        self.__check_in = check_in
        self.__check_out = check_out
        self.__status = "Confirmada"
        self.__id = str(uuid.uuid4())[:8]
    
    @property
    def id(self):
        return self.__id
    
    @property
    def cliente(self):
        return self.__cliente
    
    @property
    def quarto(self):
        return self.__quarto
    
    @property
    def check_in(self):
        return self.__check_in
    
    @property
    def check_out(self):
        return self.__check_out
    
    @property
    def status(self):
        return self.__status
    
    def cancelar(self):
        """Cancela a reserva"""
        self.__status = "Cancelada"
        self.__quarto.set_disponibilidade(True)
    
    def calcular_total(self) -> float:
        """Calcula o valor total da reserva"""
        dias = (self.__check_out - self.__check_in).days
        return dias * self.__quarto.preco_diaria
    
    def to_dict(self):
        return {
            'id': self.__id,
            'cliente': self.__cliente.to_dict(),
            'quarto': self.__quarto.to_dict(),
            'check_in': self.__check_in.isoformat(),
            'check_out': self.__check_out.isoformat(),
            'status': self.__status
        }
    
    @classmethod
    def from_dict(cls, data):
        cliente = Cliente.from_dict(data['cliente'])
        quarto = Quarto.from_dict(data['quarto'])
        check_in = datetime.fromisoformat(data['check_in']).date()
        check_out = datetime.fromisoformat(data['check_out']).date()
        reserva = cls(cliente, quarto, check_in, check_out)
        reserva.__id = data['id']
        if data['status'] == "Cancelada":
            reserva.cancelar()
        return reserva


class GerenciadorDeReservas:
    """Classe principal para gerenciar todas as operações"""
    def __init__(self):
        self.__quartos: Dict[int, Quarto] = {}
        self.__clientes: Dict[str, Cliente] = {}
        self.__reservas: Dict[str, Reserva] = {}
        self._inicializar_dados()
    
    def _inicializar_dados(self):
        """Inicializa dados de exemplo"""
        # Criar quartos
        quartos_exemplo = [
            Quarto(101, "Single", 150.00),
            Quarto(102, "Single", 150.00),
            Quarto(201, "Double", 250.00),
            Quarto(202, "Double", 250.00),
            Quarto(301, "Suite", 450.00),
            Quarto(302, "Suite", 450.00),
        ]
        
        for quarto in quartos_exemplo:
            self.__quartos[quarto.numero] = quarto
        
        # Criar clientes de exemplo
        clientes_exemplo = [
            Cliente("João Silva", "(11) 99999-1111", "joao@email.com"),
            Cliente("Maria Santos", "(11) 99999-2222", "maria@email.com"),
            Cliente("Pedro Oliveira", "(11) 99999-3333", "pedro@email.com"),
        ]
        
        for cliente in clientes_exemplo:
            self.__clientes[cliente.id] = cliente
    
    def listar_quartos_disponiveis(self) -> List[Quarto]:
        """Retorna lista de quartos disponíveis"""
        return [q for q in self.__quartos.values() if q.disponivel]
    
    def listar_todos_quartos(self) -> List[Quarto]:
        """Retorna todos os quartos"""
        return list(self.__quartos.values())
    
    def buscar_quarto(self, numero: int) -> Optional[Quarto]:
        """Busca quarto pelo número"""
        return self.__quartos.get(numero)
    
    def listar_clientes(self) -> List[Cliente]:
        """Retorna todos os clientes"""
        return list(self.__clientes.values())
    
    def adicionar_cliente(self, nome: str, telefone: str, email: str) -> Cliente:
        """Adiciona novo cliente"""
        cliente = Cliente(nome, telefone, email)
        self.__clientes[cliente.id] = cliente
        return cliente
    
    def atualizar_cliente(self, cliente_id: str, nome: str, telefone: str, email: str):
        """Atualiza dados de um cliente"""
        if cliente_id in self.__clientes:
            cliente = self.__clientes[cliente_id]
            cliente.nome = nome
            cliente.telefone = telefone
            cliente.email = email
            return True
        return False
    
    def remover_cliente(self, cliente_id: str) -> bool:
        """Remove um cliente (apenas se não tiver reservas ativas)"""
        for reserva in self.__reservas.values():
            if reserva.cliente.id == cliente_id and reserva.status == "Confirmada":
                return False
        return self.__clientes.pop(cliente_id, None) is not None
    
    def criar_reserva(self, cliente_id: str, quarto_numero: int, check_in: date, check_out: date) -> Optional[Reserva]:
        """Cria uma nova reserva"""
        cliente = self.__clientes.get(cliente_id)
        quarto = self.__quartos.get(quarto_numero)
        
        if not cliente or not quarto:
            return None
        
        if not quarto.disponivel:
            return None
        
        if check_in >= check_out:
            return None
        
        if check_in < date.today():
            return None
        
        # Verificar conflitos de datas
        for reserva in self.__reservas.values():
            if reserva.quarto.numero == quarto_numero and reserva.status == "Confirmada":
                if not (check_out <= reserva.check_in or check_in >= reserva.check_out):
                    return None
        
        reserva = Reserva(cliente, quarto, check_in, check_out)
        self.__reservas[reserva.id] = reserva
        quarto.set_disponibilidade(False)
        return reserva
    
    def cancelar_reserva(self, reserva_id: str) -> bool:
        """Cancela uma reserva existente"""
        reserva = self.__reservas.get(reserva_id)
        if reserva and reserva.status == "Confirmada":
            reserva.cancelar()
            return True
        return False
    
    def listar_reservas(self) -> List[Reserva]:
        """Retorna todas as reservas"""
        return list(self.__reservas.values())
    
    def listar_reservas_ativas(self) -> List[Reserva]:
        """Retorna reservas ativas (não canceladas)"""
        return [r for r in self.__reservas.values() if r.status == "Confirmada"]
    
    def salvar_dados(self, arquivo: str = "hotel_data.json"):
        """Salva dados em arquivo JSON"""
        dados = {
            'quartos': [q.to_dict() for q in self.__quartos.values()],
            'clientes': [c.to_dict() for c in self.__clientes.values()],
            'reservas': [r.to_dict() for r in self.__reservas.values()]
        }
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
    
    def carregar_dados(self, arquivo: str = "hotel_data.json"):
        """Carrega dados de arquivo JSON"""
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            # Carregar quartos
            self.__quartos.clear()
            for q_data in dados['quartos']:
                quarto = Quarto.from_dict(q_data)
                self.__quartos[quarto.numero] = quarto
            
            # Carregar clientes
            self.__clientes.clear()
            for c_data in dados['clientes']:
                cliente = Cliente.from_dict(c_data)
                self.__clientes[cliente.id] = cliente
            
            # Carregar reservas
            self.__reservas.clear()
            for r_data in dados['reservas']:
                reserva = Reserva.from_dict(r_data)
                self.__reservas[reserva.id] = reserva
            
            return True
        except FileNotFoundError:
            return False


# ==================== INTERFACE GRÁFICA ====================

class HotelApp:
    def __init__(self):
        self.gerenciador = GerenciadorDeReservas()
        self.gerenciador.carregar_dados()
        self.page = None
    
    def main(self, page: ft.Page):
        self.page = page
        page.title = "Refúgio dos Sonhos - Sistema de Reservas"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window.width = 1200
        page.window.height = 700
        page.window.min_width = 800
        page.window.min_height = 600
        
        # Configurar navegação
        def navegar_para(e, destino):
            page.clean()
            if destino == "inicio":
                self.tela_inicio(page)
            elif destino == "reservas":
                self.tela_visualizar_reservas(page)
            elif destino == "clientes":
                self.tela_gerenciar_clientes(page)
            elif destino == "nova_reserva":
                self.tela_nova_reserva(page)
        
        # Barra de navegação
        navbar = ft.Container(
            content=ft.Row(
                [
                    ft.Text("🏨 Refúgio dos Sonhos", size=24, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        [
                            ft.Button("Início", on_click=lambda e: navegar_para(e, "inicio")),
                            ft.Button("Nova Reserva", on_click=lambda e: navegar_para(e, "nova_reserva")),
                            ft.Button("Minhas Reservas", on_click=lambda e: navegar_para(e, "reservas")),
                            ft.Button("Clientes", on_click=lambda e: navegar_para(e, "clientes")),
                        ]
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=20,
            bgcolor=ft.Colors.BLUE_700,
        )
        
        page.add(navbar)
        self.tela_inicio(page)
    
    def tela_inicio(self, page: ft.Page):
        """Tela inicial com lista de quartos e disponibilidade"""
        content = ft.Column(
            [
                ft.Text("Quartos Disponíveis", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(height=10),
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
        
        # Criar cards para cada quarto
        quartos_grid = ft.GridView(
            expand=True,
            runs_count=2,
            max_extent=350,
            child_aspect_ratio=1.2,
            spacing=10,
            run_spacing=10,
        )
        
        for quarto in self.gerenciador.listar_todos_quartos():
            status_color = ft.Colors.GREEN if quarto.disponivel else ft.Colors.RED
            status_text = "Disponível" if quarto.disponivel else "Ocupado"
            
            card = ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Icon(ft.Icons.HOTEL, size=40),
                            ft.Text(f"Quarto {quarto.numero}", size=20, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Tipo: {quarto.tipo}"),
                            ft.Text(f"Preço: R$ {quarto.preco_diaria:.2f}/diária"),
                            ft.Container(
                                content=ft.Text(status_text, color=ft.Colors.WHITE),
                                bgcolor=status_color,
                                border_radius=10,
                                padding=5,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    padding=20,
                ),
            )
            quartos_grid.controls.append(card)
        
        content.controls.append(quartos_grid)
        
        # Adicionar estatísticas
        stats = ft.Row(
            [
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Total de Quartos", size=16),
                                ft.Text(str(len(self.gerenciador.listar_todos_quartos())), size=30, weight=ft.FontWeight.BOLD),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=20,
                        width=200,
                    )
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Quartos Disponíveis", size=16),
                                ft.Text(str(len(self.gerenciador.listar_quartos_disponiveis())), size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=20,
                        width=200,
                    )
                ),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Text("Reservas Ativas", size=16),
                                ft.Text(str(len(self.gerenciador.listar_reservas_ativas())), size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        padding=20,
                        width=200,
                    )
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
        
        content.controls.insert(1, stats)
        content.controls.insert(2, ft.Divider())
        
        page.add(content)
    
    def voltar_para_inicio(self, page: ft.Page):
        """Volta para a tela inicial"""
        page.clean()
        # Re-adicionar navbar
        self._adicionar_navbar(page)
        self.tela_inicio(page)
    
    def tela_nova_reserva(self, page: ft.Page):
        """Formulário para criar nova reserva"""
        # Variáveis para armazenar as datas
        check_in_date = [None]  # Usando lista para permitir modificação em funções aninhadas
        check_out_date = [None]
        
        # Seleção de cliente
        clientes = self.gerenciador.listar_clientes()
        cliente_options = [ft.dropdown.Option(key=c.id, text=c.nome) for c in clientes]
        
        cliente_dropdown = ft.Dropdown(
            label="Selecione o Cliente",
            options=cliente_options,
            width=300,
        )
        
        # Seleção de quarto
        quartos_disponiveis = self.gerenciador.listar_quartos_disponiveis()
        quarto_options = [ft.dropdown.Option(key=str(q.numero), text=f"Quarto {q.numero} - {q.tipo} - R$ {q.preco_diaria:.2f}") for q in quartos_disponiveis]
        
        quarto_dropdown = ft.Dropdown(
            label="Selecione o Quarto",
            options=quarto_options,
            width=400,
        )
        
        # Datas
        data_inicio = ft.DatePicker(
            first_date=date.today(),
        )
        data_fim = ft.DatePicker(
            first_date=date.today(),
        )
        
        def open_date_picker(e, picker):
            page.overlay.append(picker)
            picker.open = True
            page.update()
        
        btn_data_inicio = ft.Button(
            "Selecionar Check-in",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: open_date_picker(e, data_inicio),
        )
        btn_data_fim = ft.Button(
            "Selecionar Check-out",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: open_date_picker(e, data_fim),
        )
        
        txt_data_inicio = ft.Text("Data não selecionada")
        txt_data_fim = ft.Text("Data não selecionada")
        
        def on_data_inicio_change(e):
            if data_inicio.value:
                # Converter datetime para date
                if hasattr(data_inicio.value, 'date'):
                    check_in_date[0] = data_inicio.value.date()
                else:
                    check_in_date[0] = data_inicio.value
                txt_data_inicio.value = f"Check-in: {check_in_date[0].strftime('%d/%m/%Y')}"
                calcular_total(None)
                page.update()
        
        def on_data_fim_change(e):
            if data_fim.value:
                # Converter datetime para date
                if hasattr(data_fim.value, 'date'):
                    check_out_date[0] = data_fim.value.date()
                else:
                    check_out_date[0] = data_fim.value
                txt_data_fim.value = f"Check-out: {check_out_date[0].strftime('%d/%m/%Y')}"
                calcular_total(None)
                page.update()
        
        data_inicio.on_change = on_data_inicio_change
        data_fim.on_change = on_data_fim_change
        
        # Valor total
        txt_valor_total = ft.Text("Valor Total: R$ 0.00", size=16, weight=ft.FontWeight.BOLD)
        
        def calcular_total(e):
            if quarto_dropdown.value and check_in_date[0] and check_out_date[0]:
                quarto = self.gerenciador.buscar_quarto(int(quarto_dropdown.value))
                if quarto:
                    dias = (check_out_date[0] - check_in_date[0]).days
                    if dias > 0:
                        total = dias * quarto.preco_diaria
                        txt_valor_total.value = f"Valor Total: R$ {total:.2f}"
                        page.update()
        
        quarto_dropdown.on_change = calcular_total
        
        def criar_reserva_click(e):
            if not cliente_dropdown.value:
                page.snack_bar = ft.SnackBar(ft.Text("Selecione um cliente"), bgcolor=ft.Colors.RED)
                page.snack_bar.open = True
                page.update()
                return
            
            if not quarto_dropdown.value:
                page.snack_bar = ft.SnackBar(ft.Text("Selecione um quarto"), bgcolor=ft.Colors.RED)
                page.snack_bar.open = True
                page.update()
                return
            
            if not check_in_date[0] or not check_out_date[0]:
                page.snack_bar = ft.SnackBar(ft.Text("Selecione as datas"), bgcolor=ft.Colors.RED)
                page.snack_bar.open = True
                page.update()
                return
            
            reserva = self.gerenciador.criar_reserva(
                cliente_dropdown.value,
                int(quarto_dropdown.value),
                check_in_date[0],
                check_out_date[0]
            )
            
            if reserva:
                self.gerenciador.salvar_dados()
                page.snack_bar = ft.SnackBar(ft.Text("Reserva criada com sucesso! Redirecionando..."), bgcolor=ft.Colors.GREEN)
                page.snack_bar.open = True
                page.update()
                
                # Redirecionar para página inicial após 2 segundos
                import asyncio
                async def redirect():
                    await asyncio.sleep(2)
                    self.voltar_para_inicio(page)
                
                asyncio.create_task(redirect())
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Erro ao criar reserva. Verifique os dados."), bgcolor=ft.Colors.RED)
                page.snack_bar.open = True
                page.update()
        
        # Botão voltar
        btn_voltar = ft.Button(
            "← Voltar",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: self.voltar_para_inicio(page),
            style=ft.ButtonStyle(bgcolor=ft.Colors.GREY_300, color=ft.Colors.BLACK),
        )
        
        form = ft.Column(
            [
                btn_voltar,
                ft.Container(height=10),
                ft.Text("Nova Reserva", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(height=20),
                ft.Text("Dados do Cliente", size=18, weight=ft.FontWeight.BOLD),
                cliente_dropdown,
                ft.Container(height=20),
                ft.Text("Dados do Quarto", size=18, weight=ft.FontWeight.BOLD),
                quarto_dropdown,
                ft.Container(height=20),
                ft.Text("Datas da Reserva", size=18, weight=ft.FontWeight.BOLD),
                ft.Row([btn_data_inicio, txt_data_inicio]),
                ft.Row([btn_data_fim, txt_data_fim]),
                ft.Container(height=20),
                txt_valor_total,
                ft.Container(height=20),
                ft.Button("Confirmar Reserva", on_click=criar_reserva_click, bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        page.add(ft.Container(content=form, padding=20, expand=True))
    
    def tela_visualizar_reservas(self, page: ft.Page):
        """Tela para visualizar e cancelar reservas"""
        reservas = self.gerenciador.listar_reservas()
        
        # Botão voltar
        btn_voltar = ft.Button(
            "← Voltar",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: self.voltar_para_inicio(page),
            style=ft.ButtonStyle(bgcolor=ft.Colors.GREY_300, color=ft.Colors.BLACK),
        )
        
        if not reservas:
            content = ft.Column(
                [
                    btn_voltar,
                    ft.Container(height=20),
                    ft.Text("Nenhuma reserva encontrada.", size=16),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
            page.add(ft.Container(content=content, padding=20, expand=True))
            return
        
        reservas_list = ft.Column()
        
        for reserva in reservas:
            status_color = ft.Colors.GREEN if reserva.status == "Confirmada" else ft.Colors.RED
            
            card = ft.Card(
                content=ft.Container(
                    content=ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text(f"Reserva #{reserva.id}", size=16, weight=ft.FontWeight.BOLD),
                                    ft.Text(f"Cliente: {reserva.cliente.nome}"),
                                    ft.Text(f"Quarto: {reserva.quarto.numero} - {reserva.quarto.tipo}"),
                                    ft.Text(f"Check-in: {reserva.check_in.strftime('%d/%m/%Y')}"),
                                    ft.Text(f"Check-out: {reserva.check_out.strftime('%d/%m/%Y')}"),
                                    ft.Text(f"Valor Total: R$ {reserva.calcular_total():.2f}"),
                                ],
                                expand=True,
                            ),
                            ft.Column(
                                [
                                    ft.Container(
                                        content=ft.Text(reserva.status, color=ft.Colors.WHITE),
                                        bgcolor=status_color,
                                        border_radius=10,
                                        padding=5,
                                    ),
                                    ft.Button(
                                        "Cancelar Reserva",
                                        icon=ft.Icons.CANCEL,
                                        color=ft.Colors.RED,
                                        on_click=lambda e, r=reserva: self._cancelar_reserva(page, r),
                                        disabled=reserva.status != "Confirmada",
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.END,
                            ),
                        ],
                    ),
                    padding=20,
                ),
            )
            reservas_list.controls.append(card)
        
        content = ft.Column(
            [
                btn_voltar,
                ft.Container(height=10),
                ft.Text("Minhas Reservas", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(height=20),
                reservas_list,
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
        
        page.add(ft.Container(content=content, padding=20, expand=True))
    
    def _cancelar_reserva(self, page: ft.Page, reserva: Reserva):
        """Cancela uma reserva"""
        def confirmar_cancelamento(e):
            if self.gerenciador.cancelar_reserva(reserva.id):
                self.gerenciador.salvar_dados()
                page.snack_bar = ft.SnackBar(ft.Text("Reserva cancelada com sucesso!"), bgcolor=ft.Colors.GREEN)
                page.snack_bar.open = True
                page.update()
                # Recarregar tela
                page.clean()
                # Re-adicionar navbar
                self._adicionar_navbar(page)
                self.tela_visualizar_reservas(page)
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Erro ao cancelar reserva"), bgcolor=ft.Colors.RED)
                page.snack_bar.open = True
                page.update()
            page.dialog = None
            dlg.open = False
            page.update()
        
        dlg = ft.AlertDialog(
            title=ft.Text("Confirmar Cancelamento"),
            content=ft.Text(f"Deseja cancelar a reserva #{reserva.id} do cliente {reserva.cliente.nome}?"),
            actions=[
                ft.TextButton("Não", on_click=lambda e: self._close_dialog(page, dlg)),
                ft.TextButton("Sim", on_click=confirmar_cancelamento),
            ],
        )
        page.dialog = dlg
        dlg.open = True
        page.update()
    
    def _close_dialog(self, page: ft.Page, dlg: ft.AlertDialog):
        """Fecha o diálogo"""
        page.dialog = None
        dlg.open = False
        page.update()
    
    def _adicionar_navbar(self, page: ft.Page):
        """Adiciona a barra de navegação"""
        def navegar_para(e, destino):
            page.clean()
            self._adicionar_navbar(page)
            if destino == "inicio":
                self.tela_inicio(page)
            elif destino == "reservas":
                self.tela_visualizar_reservas(page)
            elif destino == "clientes":
                self.tela_gerenciar_clientes(page)
            elif destino == "nova_reserva":
                self.tela_nova_reserva(page)
        
        navbar = ft.Container(
            content=ft.Row(
                [
                    ft.Text("🏨 Refúgio dos Sonhos", size=24, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        [
                            ft.Button("Início", on_click=lambda e: navegar_para(e, "inicio")),
                            ft.Button("Nova Reserva", on_click=lambda e: navegar_para(e, "nova_reserva")),
                            ft.Button("Minhas Reservas", on_click=lambda e: navegar_para(e, "reservas")),
                            ft.Button("Clientes", on_click=lambda e: navegar_para(e, "clientes")),
                        ]
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=20,
            bgcolor=ft.Colors.BLUE_700,
        )
        
        page.add(navbar)
    
    def tela_gerenciar_clientes(self, page: ft.Page):
        """Tela para gerenciar clientes"""
        # Botão voltar
        btn_voltar = ft.Button(
            "← Voltar",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: self.voltar_para_inicio(page),
            style=ft.ButtonStyle(bgcolor=ft.Colors.GREY_300, color=ft.Colors.BLACK),
        )
        
        # Formulário para adicionar cliente
        txt_nome = ft.TextField(label="Nome", width=300)
        txt_telefone = ft.TextField(label="Telefone", width=300)
        txt_email = ft.TextField(label="Email", width=300)
        
        def adicionar_cliente(e):
            if not txt_nome.value or not txt_telefone.value or not txt_email.value:
                page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos"), bgcolor=ft.Colors.RED)
                page.snack_bar.open = True
                page.update()
                return
            
            try:
                cliente = self.gerenciador.adicionar_cliente(txt_nome.value, txt_telefone.value, txt_email.value)
                self.gerenciador.salvar_dados()
                page.snack_bar = ft.SnackBar(ft.Text(f"Cliente {cliente.nome} adicionado com sucesso!"), bgcolor=ft.Colors.GREEN)
                page.snack_bar.open = True
                page.update()
                
                # Limpar formulário
                txt_nome.value = ""
                txt_telefone.value = ""
                txt_email.value = ""
                
                # Recarregar lista
                self._atualizar_lista_clientes(page, clientes_list)
            except ValueError as error:
                page.snack_bar = ft.SnackBar(ft.Text(str(error)), bgcolor=ft.Colors.RED)
                page.snack_bar.open = True
                page.update()
        
        # Lista de clientes
        clientes_list = ft.Column()
        
        def _atualizar_lista_clientes(page, lista_widget):
            clientes = self.gerenciador.listar_clientes()
            lista_widget.controls.clear()
            
            for cliente in clientes:
                card = ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(cliente.nome, size=18, weight=ft.FontWeight.BOLD),
                                ft.Text(f"ID: {cliente.id}"),
                                ft.Text(f"Telefone: {cliente.telefone}"),
                                ft.Text(f"Email: {cliente.email}"),
                            ],
                            spacing=5,
                        ),
                        padding=15,
                    ),
                )
                lista_widget.controls.append(card)
            
            page.update()
        
        _atualizar_lista_clientes(page, clientes_list)
        
        content = ft.Column(
            [
                btn_voltar,
                ft.Container(height=10),
                ft.Text("Gerenciamento de Clientes", size=24, weight=ft.FontWeight.BOLD),
                ft.Container(height=20),
                ft.Text("Adicionar Novo Cliente", size=18, weight=ft.FontWeight.BOLD),
                ft.Row([txt_nome, txt_telefone, txt_email], alignment=ft.MainAxisAlignment.CENTER),
                ft.Button("Adicionar Cliente", on_click=adicionar_cliente, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
                ft.Container(height=30),
                ft.Text("Lista de Clientes", size=18, weight=ft.FontWeight.BOLD),
                ft.Container(content=clientes_list, expand=True, scroll=ft.ScrollMode.AUTO),
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        page.add(ft.Container(content=content, padding=20, expand=True, scroll=ft.ScrollMode.AUTO))


# ==================== MAIN ====================

def main(page: ft.Page):
    app = HotelApp()
    app.main(page)

if __name__ == "__main__":
    ft.app(target=main)