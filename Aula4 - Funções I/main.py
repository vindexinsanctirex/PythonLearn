# # exemplos básicos de funções
# def saudacao():
#     print("Olá! Bem-vindo ao curso de Python.")
    
# saudacao()

# def soma(a, b):
#     return a + b

# resultado = soma(5, 3)
# print("A soma de 5 e 3 é:", resultado)

# crie um programa que crie uma função chamada saudacao, ela deve receber um parâmetro nome e imprimir uma mensagem de saudação personalizada. chame a função uma vez chamando apenas o nome e outra vez chamando o nome e a mensagem personalizada.
# def saudacao(nome, mensagem="Bem-vindo ao curso de Python!"):
#     print(f"{nome}!")
#     print(f"Olá, {nome}! {mensagem}")
    
# saudacao("Ana")
# saudacao("Bruno", "Espero que você aproveite o curso!")

# usando args q kwargs em tuplas e dicionarios
def soma_numeros(*args):
    return sum(args)

resultado = soma_numeros(1, 2, 3, 4, 5)
print("A soma dos números é:", resultado)

def detalhes_pessoa(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
        
detalhes_pessoa(nome="Carlos", idade=30, cidade="São Paulo")

# crie uma função chamada analisar_numeros, ela deve receber vários números usando *args, dentro da função use um for para somar todos os números e contar quantos números foram passados, depois do for retorne a soma, quantidade e a média dos números. chame a função com 5 diferentes conjuntos de números e imprima os resultados.
def analisar_numeros(*args):
    soma = 0
    quantidade = 0
    for numero in args:
        soma += numero
        quantidade += 1
    media = soma / quantidade if quantidade > 0 else 0
    return soma, quantidade, media

soma1, qtd1, media1 = analisar_numeros(10, 20, 30)
print(f"Soma: {soma1}, Quantidade: {qtd1}, Média: {media1}")
soma2, qtd2, media2 = analisar_numeros(5, 15, 25, 35, 45)
print(f"Soma: {soma2}, Quantidade: {qtd2}, Média: {media2}")
soma3, qtd3, media3 = analisar_numeros(1, 2, 3, 4)
print(f"Soma: {soma3}, Quantidade: {qtd3}, Média: {media3}")
soma4, qtd4, media4 = analisar_numeros(100, 200)
print(f"Soma: {soma4}, Quantidade: {qtd4}, Média: {media4}")
soma5, qtd5, media5 = analisar_numeros(7, 14, 21, 28, 35, 42)
print(f"Soma: {soma5}, Quantidade: {qtd5}, Média: {media5}")