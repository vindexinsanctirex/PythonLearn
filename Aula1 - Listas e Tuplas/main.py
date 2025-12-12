# animais = ["cachorro", "gato", "papagaio", "hamster"]

# for i in animais:
#     print(i)
    
# for i in range(len(animais)):
#     print(animais[i])
    
# idades = [5, 3, 21, 18, 6, 23, 17]
# maiores_idades = []
# contador = 0

# for idade in idades:
#     if idade >= 18:
#         maiores_idades.append(idade)
#     else:
#         contador += 1
        
# maiores_idades.sort()
# maiores_idades[0] = "adulto"

# print(len(maiores_idades))

# restante = [idade for idade in idades if idade < 18]

# print(idades)
# print(maiores_idades)
# print(restante)
# print(contador)

# numeros = [6, -5, 3, 2, -8, 1, 4, -10]
# positivos = []
# negativos = []
# for numero in numeros:
#     if numero >= 0:
#         positivos.append(numero)
#     else:
#         negativos.append(numero)
        
# positivos.sort()
# negativos.sort()

# print("Números positivos:", positivos)
# print("Números negativos:", negativos)
# print("Quantidade de números positivos:", len(positivos))
# print("Quantidade de números negativos:", len(negativos))

# tupla_numeros = (10, 20, 30, 40, 50)

# primeiro_valor, segundo_valor, *outros_valores = tupla_numeros # Desempacotamento com o operador * quando usamos a tupla inteira
# primeiro_numero = tupla_numeros[0] # Acessando o primeiro valor da tupla via indexação

# print("Primeiro valor:", primeiro_valor)
# print("Segundo valor:", segundo_valor)
# print("Outros valores:", outros_valores)
# print("Primeiro número (indexação):", primeiro_numero)

# convertendo_lista = list(tupla_numeros) # Convertendo a tupla em lista
# print("Tupla convertida em lista:", convertendo_lista)

# convertendo_tupla = tuple(convertendo_lista) # Convertendo a lista de volta para tupla
# print("Lista convertida de volta para tupla:", convertendo_tupla)

produtos = (("camiseta", 2), ("calça", 9), ("tênis", 5), ("boné", 12), ("meia", 0))

for produto, quantidade in produtos:
    print(f"Produto: {produto} - Quantidade: {quantidade}")
    if quantidade == 0:
        print(f"O produto {produto} está esgotado.")
    elif quantidade < 5:
        print(f"O produto {produto} está com estoque baixo.")
    else:
        print(f"O produto {produto} está com estoque suficiente.")