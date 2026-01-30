# Lista global de produtos
produtos = []

# Dicionário para o carrinho atual
carrinho_atual = None

def cadastrar_produtos():
    """Cadastra novos produtos no sistema"""
    print("\n--- CADASTRO DE PRODUTOS ---")
    
    while True:
        try:
            id_produto = int(input("ID do produto (0 para sair): "))
            if id_produto == 0:
                break
            
            # Verificar se ID já existe
            for produto in produtos:
                if produto['id'] == id_produto:
                    print("ID já existe! Use outro ID.")
                    continue
            
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: R$ "))
            categoria = input("Categoria do produto: ")
            
            produto = {
                'id': id_produto,
                'nome': nome,
                'preco': preco,
                'categoria': categoria
            }
            
            produtos.append(produto)
            print(f"Produto '{nome}' cadastrado com sucesso!")
            
        except ValueError:
            print("Erro: Insira valores válidos!")
        except Exception as e:
            print(f"Erro inesperado: {e}")

def listar_produtos():
    """Lista todos os produtos cadastrados"""
    print("\n--- LISTA DE PRODUTOS ---")
    
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    for produto in produtos:
        print(f"ID: {produto['id']} | Nome: {produto['nome']} | "
              f"Preço: R${produto['preco']:.2f} | Categoria: {produto['categoria']}")

def comecar_um_carrinho():
    """Inicia um novo carrinho de compras"""
    global carrinho_atual
    
    carrinho_atual = {
        'produtos_carrinho': [],
        'total': 0.0
    }
    
    print("\nNovo carrinho criado com sucesso!")
    return carrinho_atual

def adicionar_produto_ao_carrinho():
    """Adiciona um produto ao carrinho atual (aumenta quantidade se já existir)"""
    global carrinho_atual
    
    if carrinho_atual is None:
        print("\nErro: Nenhum carrinho ativo. Crie um carrinho primeiro.")
        return
    
    if not produtos:
        print("\nErro: Não há produtos cadastrados.")
        return
    
    listar_produtos()
    
    try:
        id_produto = int(input("\nDigite o ID do produto que deseja adicionar: "))
        
        # Buscar produto pelo ID
        produto_encontrado = None
        for produto in produtos:
            if produto['id'] == id_produto:
                produto_encontrado = produto
                break
        
        if produto_encontrado:
            # Verificar se produto já está no carrinho
            produto_no_carrinho = None
            for item in carrinho_atual['produtos_carrinho']:
                if item['id'] == id_produto:
                    produto_no_carrinho = item
                    break
            
            try:
                quantidade = int(input(f"Quantidade de '{produto_encontrado['nome']}' (padrão: 1): ") or "1")
                if quantidade < 1:
                    quantidade = 1
            except ValueError:
                quantidade = 1
            
            if produto_no_carrinho:
                # Produto já está no carrinho - apenas aumentar quantidade
                produto_no_carrinho['quantidade'] += quantidade
                produto_no_carrinho['subtotal'] = produto_no_carrinho['preco'] * produto_no_carrinho['quantidade']
                print(f"Quantidade de '{produto_encontrado['nome']}' aumentada para {produto_no_carrinho['quantidade']}!")
            else:
                # Produto não está no carrinho - adicionar novo item
                produto_carrinho = produto_encontrado.copy()
                produto_carrinho['quantidade'] = quantidade
                produto_carrinho['subtotal'] = produto_encontrado['preco'] * quantidade
                
                carrinho_atual['produtos_carrinho'].append(produto_carrinho)
                print(f"Produto '{produto_encontrado['nome']}' adicionado ao carrinho!")
            
            # Atualizar o total do carrinho
            carrinho_atual['total'] = calcular_total_carrinho()
            
        else:
            print("Produto não encontrado!")
            
    except ValueError:
        print("Erro: ID deve ser um número inteiro!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def remover_item_pedido():
    """Remove um produto do carrinho ou reduz sua quantidade"""
    global carrinho_atual
    
    if carrinho_atual is None or not carrinho_atual['produtos_carrinho']:
        print("\nCarrinho vazio ou não iniciado.")
        return
    
    # Mostrar produtos no carrinho
    print("\n--- PRODUTOS NO CARRINHO ---")
    for i, produto in enumerate(carrinho_atual['produtos_carrinho'], 1):
        print(f"{i}. {produto['nome']} - Quantidade: {produto['quantidade']} - Subtotal: R${produto['subtotal']:.2f}")
    
    try:
        opcao = input("\nDigite o número do produto que deseja remover (ou '0' para cancelar): ")
        
        if opcao == "0":
            return
        
        indice = int(opcao) - 1
        
        if 0 <= indice < len(carrinho_atual['produtos_carrinho']):
            produto = carrinho_atual['produtos_carrinho'][indice]
            
            print(f"\nProduto selecionado: {produto['nome']}")
            print(f"Quantidade atual: {produto['quantidade']}")
            
            while True:
                try:
                    quantidade_remover = int(input(f"Quantidade para remover (1-{produto['quantidade']}, ou {produto['quantidade']} para remover todos): "))
                    
                    if 1 <= quantidade_remover <= produto['quantidade']:
                        if quantidade_remover == produto['quantidade']:
                            # Remover o produto completamente
                            produto_removido = carrinho_atual['produtos_carrinho'].pop(indice)
                            print(f"Produto '{produto_removido['nome']}' removido completamente do carrinho!")
                        else:
                            # Reduzir apenas a quantidade
                            produto['quantidade'] -= quantidade_remover
                            produto['subtotal'] = produto['preco'] * produto['quantidade']
                            print(f"Quantidade de '{produto['nome']}' reduzida para {produto['quantidade']}!")
                        
                        # Atualizar o total do carrinho
                        carrinho_atual['total'] = calcular_total_carrinho()
                        break
                    else:
                        print(f"Quantidade inválida! Digite um valor entre 1 e {produto['quantidade']}.")
                        
                except ValueError:
                    print("Digite um número válido!")
        else:
            print("Opção inválida!")
            
    except ValueError:
        print("Erro: Digite um número válido!")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def calcular_total_carrinho():
    """Calcula o total do carrinho"""
    if carrinho_atual is None:
        return 0.0
    
    total = 0.0
    for produto in carrinho_atual['produtos_carrinho']:
        total += produto['subtotal']
    
    return total

def mostrar_resumo_do_pedido():
    """Mostra o resumo do pedido atual"""
    global carrinho_atual
    
    if carrinho_atual is None or not carrinho_atual['produtos_carrinho']:
        print("\nCarrinho vazio ou não iniciado.")
        return
    
    print("\n--- RESUMO DO PEDIDO ---")
    print("Produtos no carrinho:")
    print("-" * 50)
    
    for produto in carrinho_atual['produtos_carrinho']:
        print(f"{produto['nome']} (x{produto['quantidade']})")
        print(f"  Preço unitário: R${produto['preco']:.2f}")
        print(f"  Subtotal: R${produto['subtotal']:.2f}")
        print("-" * 30)
    
    print(f"\nTOTAL DO PEDIDO: R${carrinho_atual['total']:.2f}")

def menu_principal():
    """Menu principal do sistema"""
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE VENDAS")
        print("="*50)
        print("1. Cadastrar produtos")
        print("2. Listar produtos")
        print("3. Começar um carrinho")
        print("4. Adicionar produto ao carrinho")
        print("5. Remover item do pedido")
        print("6. Mostrar resumo do pedido")
        print("7. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            cadastrar_produtos()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            comecar_um_carrinho()
        elif opcao == "4":
            adicionar_produto_ao_carrinho()
        elif opcao == "5":
            remover_item_pedido()
        elif opcao == "6":
            mostrar_resumo_do_pedido()
        elif opcao == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Adicionando alguns produtos de exemplo para teste
produtos.extend([
    {'id': 1, 'nome': 'Camiseta', 'preco': 29.90, 'categoria': 'Vestuário'},
    {'id': 2, 'nome': 'Calça Jeans', 'preco': 89.90, 'categoria': 'Vestuário'},
    {'id': 3, 'nome': 'Tênis', 'preco': 129.90, 'categoria': 'Calçados'},
    {'id': 4, 'nome': 'Notebook', 'preco': 2499.90, 'categoria': 'Eletrônicos'}
])

# Iniciar o sistema
if __name__ == "__main__":
    menu_principal()