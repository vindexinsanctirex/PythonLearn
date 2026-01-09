# Cria um dicionário vazio para armazenar produtos e preços
produtos = {}

print("Digite os dados de 5 produtos:")

# Loop para inserir 5 produtos
contador = 1
while len(produtos) < 5:
    try:
        print(f"\nProduto {contador}:")
        nome = input("Nome do produto: ").strip()
        
        # Verifica se o nome não está vazio
        if not nome:
            print("Erro: O nome do produto não pode estar vazio!")
            continue
        
        # Tenta converter o preço para float
        preco_str = input("Preço do produto: R$ ").replace(',', '.').strip()
        preco = float(preco_str)
        
        # Verifica se o preço é positivo
        if preco < 0:
            print("Erro: O preço não pode ser negativo!")
            continue
        
        # Armazena no dicionário
        produtos[nome] = preco
        contador += 1
        
    except ValueError:
        print("Erro: Digite um preço válido! (Ex: 10.50 ou 10,50)")

# Calcula o valor total da compra
total = sum(produtos.values())

# Exibe os produtos e o valor total
print("\n" + "="*50)
print("RESUMO DA COMPRA".center(50))
print("="*50)

for produto, preco in produtos.items():
    print(f"• {produto:30} R$ {preco:>8.2f}")

print("-"*50)
print(f"{'TOTAL:':30} R$ {total:>8.2f}")
print("="*50)