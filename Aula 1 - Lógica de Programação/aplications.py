# # Sistema de Vendas Simplificado

# qtd = int(input("Quantos produtos vendeu hoje? "))

# nomes = []
# pesos = []
# precos_kg = []
# precos_totais = []

# for i in range(qtd):
#     print(f"\nProduto {i+1}:")
#     nome = input("Nome: ")
#     peso = float(input("Peso (kg): "))
#     preco_kg_valor = float(input("Preço por kg: R$ "))
    
#     nomes.append(nome)
#     pesos.append(peso)
#     precos_kg.append(preco_kg_valor)
#     precos_totais.append(peso * preco_kg_valor)

# # Relatório
# print("\n=== VENDAS DO DIA ===")
# for i in range(qtd):
#     print(f"{nomes[i]}: {pesos[i]}kg × R$ {precos_kg[i]} = R$ {precos_totais[i]:.2f}")

# # Maior e menor peso
# maior = pesos[0]
# menor = pesos[0]

# for peso in pesos:
#     maior = max(maior, peso)
#     menor = min(menor, peso)

# print(f"\nMaior peso: {maior}kg")
# print(f"Menor peso: {menor}kg")

# # Total
# total = 0
# for preco in precos_totais:
#     total += preco

# print(f"Total vendido: R$ {total:.2f}")

# qtd = int(input("Quantos produtos? "))

# pesos = []
# precos = []

# for i in range(qtd):
#     p = float(input("Peso (kg): "))
#     pk = float(input("Preço/kg: R$ "))
#     pesos.append(p)
#     precos.append(p * pk)

# print(f"\nMaior: {max(pesos)}kg")
# print(f"Menor: {min(pesos)}kg")
# print(f"Média: {sum(pesos)/len(pesos):.2f}kg") 
# print(f"Total: R$ {sum(precos):.2f}")

animais = ["cachorro", "gato", "elefante", "leão", "tigre", "gato", "gato", "coelho", "gato", "papagaio", "gato"]

print ("há", animais.count("gato"), "gatos na lista")
print ("Há ", animais.count("cachorro"), "cachorros na lista")
print("o leão está na posição", animais.index("leão"))
print("o elefante está na posição", animais.index("elefante"))
animais.sort()
print(animais)