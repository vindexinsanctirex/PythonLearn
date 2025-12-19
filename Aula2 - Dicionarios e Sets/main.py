# # dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'} com loop for

# dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
# for chave, valor in dicionario.items():
#     print(f"Chave: {chave}, Valor: {valor}")

# # set union, intersection, difference, symmetric difference
# set1 = {7, 9, 5, 2, 3}
# set2 = {10, 12, 4, 3, 5}
# union_set = set1.union(set2)
# intersection_set = set1.intersection(set2)
# difference_set = set1.difference(set2)
# symmetric_difference_set = set1.symmetric_difference(set2)
# print("Union:", union_set)
# print("Intersection:", intersection_set)
# print("Difference:", difference_set)
# print("Symmetric Difference:", symmetric_difference_set)

# # operadorees matemáticos em sets
# set1 = {7, 9, 5, 2, 3}
# set2 = {10, 12, 4, 3, 5}
# union_set = set1 | set2
# intersection_set = set1 & set2
# difference_set = set1 - set2
# symmetric_difference_set = set1 ^ set2

# print("Union:", union_set)
# print("Intersection:", intersection_set)
# print("Difference:", difference_set)
# print("Symmetric Difference:", symmetric_difference_set)

# matematica = {'João', 'Maria', 'Carlos', 'Ana', 'Romero', 'Pedro', 'Fernanda', 'Ricardo'}
# fisica = {'Carlos', 'Ana', 'Pedro', 'Fernanda', 'João', 'Rui', 'Rafael', 'Roger'}

# # adicionar um elemento a um set
# matematica.add('Ricardo')
# fisica.update(['Rui', 'Rafael', 'Nobre'])

# # remover um elemento de um set
# matematica.remove('Ana')
# matematica.discard('João')
# fisica.pop()
# print("Aluno reprovado: ", fisica.pop())

# ambas = matematica.intersection(fisica)

# matematica.intersection_update(fisica)

# print(matematica)
# print(ambas)

# print(matematica.union(fisica))

# apenas_matematica = matematica.difference(fisica)

# um_ou_outro = matematica ^ fisica
# print(um_ou_outro)

# sorteio com set

participantes = {'João', 'Maria', 'Carlos', 'Ana', 'Romero', 'Pedro', 'Fernanda', 'Ricardo'}
premiados = set()

for i in range(3):
    premiado = participantes.pop()
    premiados.add(premiado)
    
print("Premiados:", premiados)

perdedores = participantes - premiados

print("Perdedores:", perdedores)