#  todos os exemplos de condicionais estão aqui

# Exemplo 1: Verificar se um número é par ou ímpar
numero = 10
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
    
# Exemplo 2: Verificar se um número é positivo, negativo ou zero
numero = -5
if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"O número é zero.")
    
# Exemplo 3: Verificar se uma pessoa é maior de idade
idade = 17
if idade >= 18:
    print("A pessoa é maior de idade.")
else:
    print("A pessoa é menor de idade.")
    
# Exemplo 4: Verificar se um ano é bissexto
ano = 2020
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

# Exemplo 5: Verificar se um caractere é uma vogal ou consoante
caractere = 'a'
if caractere.lower() in 'aeiou':
    print(f"O caractere '{caractere}' é uma vogal.")
else:
    print(f"O caractere '{caractere}' é uma consoante.")
    
# Exemplo 6: Verificar se um número está dentro de um intervalo
numero = 15
if 10 <= numero <= 20:
    print(f"O número {numero} está dentro do intervalo de 10 a 20.")
else:
    print(f"O número {numero} está fora do intervalo de 10 a 20.")
    
# Exemplo 7: Verificar se uma string é vazia
texto = ""
if texto:
    print("A string não é vazia.")
else:
    print("A string é vazia.")
    
# Exemplo 8: Verificar se um número é múltiplo de outro
num1 = 15
num2 = 5
if num1 % num2 == 0:
    print(f"O número {num1} é múltiplo de {num2}.")
else:
    print(f"O número {num1} não é múltiplo de {num2}.")
    
# Exemplo 9: Verificar se um caractere é maiúsculo ou minúsculo
caractere = 'G'
if caractere.isupper():
    print(f"O caractere '{caractere}' é maiúsculo.")
else:
    print(f"O caractere '{caractere}' é minúsculo.")
    
# Exemplo 10: Verificar senha de acesso
senha_correta = "senha123"
senha_digitada = "senha123"
if senha_digitada == senha_correta:
    print("Acesso permitido.")
else:
    print("Acesso negado.")
    
# Exemplo 11: Verificar se uma lista contém um elemento
lista = [1, 2, 3, 4, 5]
elemento = 3
if elemento in lista:
    print(f"O elemento {elemento} está na lista.")
else:
    print(f"O elemento {elemento} não está na lista.")
    
# Exemplo 12: Verificar se um número é primo
numero = 7
if numero > 1:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            print(f"O número {numero} não é primo.")
            break
    else:
        print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
    
# Exemplo 13: Verificar se um ano é século 20.
ano = 1950
if 1901 <= ano <= 2000:
    print(f"O ano {ano} pertence ao século 20.")
else:
    print(f"O ano {ano} não pertence ao século 20.")
    
# Exemplo 14: Operações com == e !=
valor1 = 10
valor2 = 20
if valor1 == valor2:
    print("Os valores são iguais.")
else:
    print("Os valores são diferentes.")
if valor1 != valor2:
    print("Os valores são diferentes.")
else:
    print("Os valores são iguais.")