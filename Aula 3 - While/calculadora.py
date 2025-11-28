# calculadora que faça também cálculo de área de diferentes formas geométricas, rodando em loop até o usuário desejar sair
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
        return "Erro: Divisão por zero não é permitida."
def area_retangulo(base, altura):
    return base * altura
def area_triangulo(base, altura):
    return (base * altura) / 2
def area_circulo(raio):
    import math
    return math.pi * raio ** 2
while True:
    print("\nCalculadora:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Área do Retângulo")
    print("6. Área do Triângulo")
    print("7. Área do Círculo")
    print("8. Sair")
    escolha = input("Escolha uma opção (1-8): ")
    if escolha == '8':
        print("Saindo da calculadora.")
        break
    elif escolha in ['1', '2', '3', '4']:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if escolha == '1':
            print(f"Resultado: {soma(a, b)}")
        elif escolha == '2':
            print(f"Resultado: {subtracao(a, b)}")
        elif escolha == '3':
            print(f"Resultado: {multiplicacao(a, b)}")
        elif escolha == '4':
            print(f"Resultado: {divisao(a, b)}")
    elif escolha == '5':
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        print(f"Área do Retângulo: {area_retangulo(base, altura)}")
    elif escolha == '6':
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        print(f"Área do Triângulo: {area_triangulo(base, altura)}")
    elif escolha == '7':
        raio = float(input("Digite o raio do círculo: "))
        print(f"Área do Círculo: {area_circulo(raio)}")
    else:
        print("Opção inválida. Tente novamente.")
        
