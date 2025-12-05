# # for e range
# for numero in range(1, 11):
#     print(numero)
    
# # for e string
# for letra in 'Python':
#     print(letra)
    
# # lista com 5 elementos, exibir todos, depois último elemento
# lista = [10, 20, 30, 40, 50]
# for elemento in lista:
#     print(elemento)
# print('Último elemento:', lista[-1])

# palavra = 'Programação'
# for letra in range(len(palavra)):
#     print(palavra[letra])
# print('Última letra:', palavra[-1])

# frutas = ['maçã', 'banana', 'laranja', 'uva']
# for fruta in frutas:
#     if fruta == 'laranja':
#         continue
#         print('Encontrei a laranja!')
#         # break
#     print('Fruta atual:', fruta)
# print('Fim da busca pelas frutas.')

# for numero in range(23, -23, -6):
#     print('Número atual:', numero)

# for numero in range(1, 11):
#     print('Número atual:', numero)
    

# numero = input('Digite um número: ')
# for digito in range(1, 11):
#     print(f'{numero} x {digito} = {int(numero) * digito}')
    
# # acumulador variável de soma de 1 a 100
# soma = 0
# for numero in range(1, 101):
#     soma += numero
# print('Soma de 1 a 100:', soma)

#fatorial de input
n = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1
for numero in range(1, n + 1):
    fatorial *= numero
print(f'O fatorial de {n} é {fatorial}')