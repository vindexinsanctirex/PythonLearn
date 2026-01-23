# funções somar e subtrair que recebam dois números e retorne o resultado
def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b
# função calcular que receba dois números e uma função (somar ou subtrair) e retorne o resultado da operação
def calcular(a, b, operacao):
    return operacao(a, b)
# exemplos de uso
resultado_soma = calcular(10, 5, somar)
print(f"Resultado da soma: {resultado_soma}")  # Resultado da soma: 15
resultado_subtracao = calcular(10, 5, subtrair)
print(f"Resultado da subtração: {resultado_subtracao}")  # Resultado da subtração: 5
# funções dobro e quadrado que recebam um número e retornem o dobro e o quadrado desse número, respectivamente
def dobro(x):
    return x * 2
def quadrado(x):
    return x ** 2
# função aplicar que receba um número e uma função (dobro ou quadrado) e retorne o resultado da aplicação
def aplicar(x, funcao):
    return funcao(x)
# exemplos de uso
resultado_dobro = aplicar(4, dobro)
print(f"Resultado do dobro: {resultado_dobro}")  # Resultado do dobro: 8
resultado_quadrado = aplicar(4, quadrado)
print(f"Resultado do quadrado: {resultado_quadrado}")  # Resultado do quadrado: 16