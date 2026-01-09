# listas
nomes = ['Ana', 'Bruno', 'Carlos', 'Diana']
idades = [23, 30, 25, 28]
# dicionários
pessoa1 = {'nome': 'Ana', 'idade': 23, 'cidade': 'São Paulo'}
pessoa2 = {'nome': 'Bruno', 'idade': 30, 'cidade': 'Rio de Janeiro'}
# tuplas
coordenadas = (10.0, 20.0)
# conjuntos
frutas = {'maçã', 'banana', 'laranja'}
# imprimindo os dados
print("Nomes:", nomes)
print("Idades:", idades)
print("Pessoa 1:", pessoa1)
print("Pessoa 2:", pessoa2)
print("Coordenadas:", coordenadas)
print("Frutas:", frutas)
# operações básicas
# listas
nomes.append('Eduardo')
print("Nomes após adição:", nomes)
# dicionários
pessoa1['profissão'] = 'Engenheira'
print("Pessoa 1 após adição:", pessoa1)
# tuplas (imutáveis, não podem ser alteradas)
# conjuntos
frutas.add('uva')
print("Frutas após adição:", frutas)
# acesso a elementos
print("Primeiro nome:", nomes[0])
print("Idade de Bruno:", pessoa2['idade'])
print("Primeira coordenada:", coordenadas[0])
print("Frutas disponíveis:", frutas)
# remoção de elementos
nomes.remove('Carlos')
print("Nomes após remoção:", nomes)
del pessoa2['cidade']
print("Pessoa 2 após remoção:", pessoa2)
frutas.remove('banana')
print("Frutas após remoção:", frutas)
# verificando existência
print("Ana está na lista de nomes?", 'Ana' in nomes)
print("Bruno está no dicionário pessoa2?", 'Bruno' == pessoa2.get('nome'))
print("Coordenada (10.0, 20.0) existe?", coordenadas == (10.0, 20.0))
print("Maçã está no conjunto de frutas?", 'maçã' in frutas)
