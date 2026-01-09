# # listas
# nomes = ['Ana', 'Bruno', 'Carlos', 'Diana']
# idades = [23, 30, 25, 28]
# # dicionários
# pessoa1 = {'nome': 'Ana', 'idade': 23, 'cidade': 'São Paulo'}
# pessoa2 = {'nome': 'Bruno', 'idade': 30, 'cidade': 'Rio de Janeiro'}
# # tuplas
# coordenadas = (10.0, 20.0)
# # conjuntos
# frutas = {'maçã', 'banana', 'laranja'}
# # imprimindo os dados
# print("Nomes:", nomes)
# print("Idades:", idades)
# print("Pessoa 1:", pessoa1)
# print("Pessoa 2:", pessoa2)
# print("Coordenadas:", coordenadas)
# print("Frutas:", frutas)
# # operações básicas
# # listas
# nomes.append('Eduardo')
# print("Nomes após adição:", nomes)
# # dicionários
# pessoa1['profissão'] = 'Engenheira'
# print("Pessoa 1 após adição:", pessoa1)
# # tuplas (imutáveis, não podem ser alteradas)
# # conjuntos
# frutas.add('uva')
# print("Frutas após adição:", frutas)
# # acesso a elementos
# print("Primeiro nome:", nomes[0])
# print("Idade de Bruno:", pessoa2['idade'])
# print("Primeira coordenada:", coordenadas[0])
# print("Frutas disponíveis:", frutas)
# # remoção de elementos
# nomes.remove('Carlos')
# print("Nomes após remoção:", nomes)
# del pessoa2['cidade']
# print("Pessoa 2 após remoção:", pessoa2)
# frutas.remove('banana')
# print("Frutas após remoção:", frutas)
# # verificando existência
# print("Ana está na lista de nomes?", 'Ana' in nomes)
# print("Bruno está no dicionário pessoa2?", 'Bruno' == pessoa2.get('nome'))
# print("Coordenada (10.0, 20.0) existe?", coordenadas == (10.0, 20.0))
# print("Maçã está no conjunto de frutas?", 'maçã' in frutas)


# # crie uma lista de números inteiros com pelo menos 5 valores, mostre todos números da lista usando for, calcule e exiba a soma de todos os números, mostre apenas os números maiores que 10, verifique com if e else se a lista tem mais de 5 elementos ou não, e exiba todas as informações em f-strings.

# numeros = [5, 12, 7, 20, 3, 15]
# soma_numeros = sum(numeros)
# print(f"Números na lista: {numeros}")
# print(f"Soma de todos os números: {soma_numeros}")
# print("Números maiores que 10:")
# for numero in numeros:
#     if numero > 10:
#         print(f"- {numero}")
# if len(numeros) > 5:
#     print(f"A lista tem mais de 5 elementos. Total de elementos: {len(numeros)}")
# else:
#     print(f"A lista tem 5 ou menos elementos. Total de elementos: {len(numeros)}")
    
    
# # tuplas
# tupla_exemplo = (1, 2, 3, 4, 5)
# print(f"Tupla exemplo: {tupla_exemplo}")
# print(f"Elemento na posição 2 da tupla: {tupla_exemplo[2]}")
# # desampacotamento de tuplas
# a, b, c, d, e = tupla_exemplo
# print(f"Desempacotamento: a={a}, b={b}, c={c}, d={d}, e={e}")
# # desacoplar com *
# numeros_desacoplados = (10, 20, 30, 40, 50)
# x, y, *resto = numeros_desacoplados
# print(f"x={x}, y={y}, resto={resto}")

# crie uma tupla com nomes de frutasc(mínimo 4), mostre todas as frutas usando for, conte quantas frutas existem na tupla, verifique com if e else se a fruta 'banana' está na tupla ou não, e exiba se tem mais de 3 frutas ou não e exiba todas as informações em f-strings.

# frutas = ('maçã', 'banana', 'laranja', 'uva', 'pera')
# print("Frutas na tupla:")
# for fruta in frutas:
#     print(f"- {fruta}")
# quantidade_frutas = len(frutas)
# print(f"Quantidade de frutas na tupla: {quantidade_frutas}")
# if 'banana' in frutas:
#     print(f"A fruta 'banana' está na tupla.")
# else:
#     print(f"A fruta 'banana' não está na tupla.")
# if quantidade_frutas > 3:
#     print(f"A tupla tem mais de 3 frutas.")
# else:
#     print(f"A tupla tem 3 ou menos frutas.")
    
    
# clientes = ['Ana', 'Carlos', 'Beatriz']

# # Com enumerate (ideal)
# for posicao, cliente in enumerate(clientes, 1):
#     print(f"Cliente {posicao}: {cliente}")

# # Com range (menos legível)
# for i in range(len(clientes)):
#     print(f"Cliente {i+1}: {clientes[i]}")


# dicionários

# # Cria um dicionário vazio para armazenar produtos e preços
# produtos = {}
# print("Digite os dados de 5 produtos:")
# # Loop para inserir 5 produtos
# contador = 1
# while len(produtos) < 5:
#     nome = input(f"\nProduto {contador} - Nome do produto: ").strip()
#     preco_str = input("Preço do produto: R$ ").replace(',', '.').strip()
#     try:
#         preco = float(preco_str)
#         produtos[nome] = preco
#         contador += 1
#     except ValueError:
#         print("Erro: Digite um preço válido! (Ex: 10.50 ou 10,50)")
        
# # Calcula o valor total da compra
# total = sum(produtos.values())

# # Exibe os produtos e o valor total
# print("\n" + "="*50)
# print("RESUMO DA COMPRA".center(50))
# print("="*50)

# for produto, preco in produtos.items():
#     print(f"• {produto:30} R$ {preco:>8.2f}")
# print("-"*50)
# print(f"{'TOTAL:':30} R$ {total:>8.2f}")
# print("="*50)

# # dicionários regras básicas
# produtos = {'banana': 3.50, 'maçã': 4.20, 'laranja': 2.80}
# # Acessando valores
# print(f"Preço da maçã: R$ {produtos['maçã']:.2f}")
# # Adicionando um novo produto
# produtos['uva'] = 5.00
# print("Produto 'uva' adicionado.")
# # Atualizando o preço de um produto
# produtos['banana'] = 3.80
# print("Preço da 'banana' atualizado.")
# # # Removendo um produto
# # del produtos['laranja']
# # print("Produto 'laranja' removido.")
# # Verificando existência de um produto
# if 'maçã' in produtos:
#     print("A maçã está disponível.")
# else:
#     print("A maçã não está disponível.")
# # Exibindo todos os produtos e preços
# print("\nLista de produtos e preços:")
# for produto, preco in produtos.items():
#     print(f"- {produto}: R$ {preco:.2f}")

# # compreheensions

# idades = [23, 30, 25, 28, 35, 40, 19]
# # Filtra idades maiores que 25 usando list comprehension
# idades_maiores_25 = {idade: idade > 25 for idade in idades if idade > 25}
# print(f"Todas as idades: {idades}")
# print(f"Idades maiores que 25: {idades_maiores_25}")

# # mostrar apenas chaves e/ou valores de um dicionário criado com comprehension
# pessoas = {'Ana': 23, 'Bruno': 30, 'Carlos': 25, 'Diana': 28}
# # Apenas chaves
# chaves = [nome for nome in pessoas.keys()]
# # Apenas valores
# valores = [idade for idade in pessoas.values()]
# print(f"Pessoas: {pessoas}")
# print(f"Chaves (nomes): {chaves}")
# print(f"Valores (idades): {valores}")

# aluno = {'nome': 'João',
# 'curso': 'Engenharia',
# 'idade': 21,
# 'cidade': 'São Paulo'}

# aluno.update({'idade': 22, 'ano': 2})
# print(aluno)

# crie um dicionário representando um aluno com as seguintes informações: nome, idade, nota. exiba todas as chaves e valores do dicionário usando for, verifique com if e else se a nota é maior ou igual a 7, mostre 'aprovado', caso contrário, mostre 'reprovado', verifique se o aluno é maior de idade, use operadores de comparação e and para exibir aluno maior de idade e aprovado quando for o caso, e exiba todas as informações em f-strings.

# aluno = {'nome': 'João', 'idade': 21, 'nota': 8.5}
# print("Informações do aluno:")
# for chave, valor in aluno.items():
#     print(f"- {chave.capitalize()}: {valor}")
# if aluno['nota'] >= 7:
#     status_nota = 'Aprovado'
# else:
#     status_nota = 'Reprovado'
# print(f"Status da nota: {status_nota}")
# if aluno['idade'] >= 18 and aluno['nota'] >= 7:
#     print(f"O aluno {aluno['nome']} é maior de idade e está aprovado.")
    
# # ou

# if aluno['idade'] >= 18 and aluno['nota'] >= 7:
#     aluno['status'] = (f"O aluno {aluno['nome']} é maior de idade e foi aprovado.")
# else:
#     aluno['status'] = (f"O aluno {aluno['nome']} é menor de idade ou foi reprovado.")
    
# for chave, valor in aluno.items():
#     print(f"- {chave.capitalize()}: {valor}")

# sets - conjuntos

# # Cria um conjunto vazio para armazenar números únicos

# numeros_unicos = set()
# print("Digite 5 números inteiros (números repetidos serão ignorados):")
# # Loop para inserir 5 números únicos
# while len(numeros_unicos) < 5:
#     try:
#         numero_str = input(f"Número {len(numeros_unicos)+1}: ").strip()
#         numero = int(numero_str)
#         if numero in numeros_unicos:
#             print("Número já inserido, por favor digite um número diferente.")
#         else:
#             numeros_unicos.add(numero)
#     except ValueError:
#         print("Erro: Digite um número inteiro válido!")
        
# # Exibe os números únicos inseridos
# print("\nNúmeros únicos inseridos:")
# for numero in sorted(numeros_unicos):
#     print(f"- {numero}")
    
    
# # intersecção, união e diferença
# conjunto_a = {1, 2, 3, 4, 5}
# conjunto_b = {4, 5, 6, 7, 8}
# # Intersecção
# intersecao = conjunto_a & conjunto_b
# print(f"Intersecção: {intersecao}")
# # União
# uniao = conjunto_a | conjunto_b
# print(f"União: {uniao}")
# # Diferença
# diferenca = conjunto_a - conjunto_b
# print(f"Diferença (A - B): {diferenca}")


# sorteio = conjunto_a.pop()
# print(f"Número sorteado do conjunto A: {sorteio}") # era pra ser aleatório, mas mas só funciona com strings

# crie um set de números inteiros com valores repetidos, mostre todos os valores do set usando for, exiba a quantidade de elementos do set, verifique com if e else se o número 10 está presente no set ou não, crie um segundo set com outros números, gere e exiba a união dos dois sets e a interseção dos dois sets, use f-string para todos os prints
numeros = {1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9}
print("Números no set:")
for numero in numeros:
    print(f"- {numero}")
quantidade_elementos = len(numeros)
print(f"Quantidade de elementos no set: {quantidade_elementos}")
if 10 in numeros:
    print("O número 10 está presente no set.")
else:
    print("O número 10 não está presente no set.")
outro_set = {5, 6, 7, 10, 11}
uniao_sets = numeros | outro_set
intersecao_sets = numeros & outro_set
print(f"União dos dois sets: {uniao_sets}")
print(f"Interseção dos dois sets: {intersecao_sets}")
if 10 in outro_set:
    print("O número 10 está presente no outro set.")
else:
    print("O número 10 não está presente no set.")