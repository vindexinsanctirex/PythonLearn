# função calculadora com três paramêtros: dois números e uma função de processamento responsável pela operação matemática
def calculadora(num1, num2, func_processamento):
    return func_processamento(num1, num2)
# funções de processamento para as operações matemáticas
def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"
def porcentagem(a, b):
    return (a * b) / 100
# função processar_lista que receba uma lista de números e uma função callback que define o critério de filtro retornando apenas os valores definidos no callback
def processar_lista(lista, func_callback):
    return [item for item in lista if func_callback(item)]
# funções callback para diferentes critérios de filtro, que são "números maiores que 10", "números pares", "números ímpares", "números positivos" e "números negativos"
def maior_que_10(num):
    return num > 10
def numeros_pares(num):
    return num % 2 == 0
def numeros_impares(num):
    return num % 2 != 0
def numeros_positivos(num):
    return num > 0
def numeros_negativos(num):
    return num < 0
# exemplos de uso da função calculadora
print(calculadora(10, 5, soma))            # Saída: 15
print(calculadora(10, 5, subtracao))       # Saída: 5
print(calculadora(10, 5, multiplicacao))   # Saída: 50
print(calculadora(10, 5, divisao))         # Saída: 2.0
print(calculadora(200, 10, porcentagem))  # Saída: 20.0
# exemplos de uso da função processar_lista
numeros = [5, 12, -3, 7, 20, -15, 8, 0, -1, 14]
print(processar_lista(numeros, maior_que_10))    # Saída: [12, 20, 14]
print(processar_lista(numeros, numeros_pares))    # Saída: [12, 20, 8, 0, 14]
print(processar_lista(numeros, numeros_impares))   # Saída: [5, -3, 7, -15, -1]
print(processar_lista(numeros, numeros_positivos))  # Saída: [5, 12, 7, 20, 8, 14]
print(processar_lista(numeros, numeros_negativos))  # Saída: [-3, -15, -1]
