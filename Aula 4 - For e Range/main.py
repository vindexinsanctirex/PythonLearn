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
    

numero = input('Digite um número: ')
for digito in range(1, 11):
    print(f'{numero} x {digito} = {int(numero) * digito}')