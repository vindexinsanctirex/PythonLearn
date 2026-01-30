# def saudacao(nome = 'Senhor'):
#     print(f"Bem-Vindo {nome}!")


# saudacao()    
# saudacao('Caio')
# saudacao(42)


# def dobro(*nums):
#     for i in nums:
#         print(i*2)

# dobro(3,4,5,6,7,20)

# def mostrar_dados(**dados):
#     for chave, valor in dados.items():
#         print(f"{chave} ~ {valor}")
        
# mostrar_dados(nome = "Gal", idade = 43, cidade='Heinder')

# def double(*nums):
#     nova_lista = []
#     for i in nums:
#         num = i*2
#         nova_lista.append(num)
#     return nova_lista

# res = double(3,4,5,6,7,20)

# print(res)

# # ou para tuplas

# def double(*nums):
#     nova_lista = []
#     for i in nums:
#         num = i*2
#         nova_lista.append(num)
#     nova_tupla = tuple(nova_lista)
#     return nova_tupla

# res = double(3,4,5,6,7,20)

# print(res)

km = 0

def acelerar():
    global km
    km += 10
    
acelerar()
acelerar()
acelerar()
acelerar()
acelerar()

print(km)