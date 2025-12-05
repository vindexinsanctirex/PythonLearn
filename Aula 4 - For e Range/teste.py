print("=== Soma dos Números Pares no Intervalo ===")
print("Digite o início e o fim do intervalo (inclusive)")

# Solicita os limites do intervalo
try:
    inicio = int(input("Digite o número inicial do intervalo: "))
    fim = int(input("Digite o número final do intervalo: "))
except ValueError:
    print("Erro: Por favor, digite números inteiros válidos!")
    exit()

# Garante que 'inicio' seja menor ou igual a 'fim'
if inicio > fim:
    inicio, fim = fim, inicio  # Troca os valores se necessário
    print(f"Intervalo ajustado: de {inicio} a {fim} (inclusive)")

# Inicializa a variável de soma
soma_pares = 0
contador_pares = 0

print(f"\nAnalisando números pares no intervalo de {inicio} a {fim}...")

# Loop for para percorrer o intervalo
for numero in range(inicio, fim + 1):
    if numero % 2 == 0:  # Verifica se o número é par
        soma_pares += numero
        contador_pares += 1
        print(f"  Número par encontrado: {numero}")
else:
    # Este bloco else executa após o loop terminar normalmente
    if contador_pares == 0:
        print("\nNão há números pares no intervalo especificado.")
    else:
        print(f"\nForam encontrados {contador_pares} número(s) par(es) no intervalo.")

# Exibe o resultado da soma
if contador_pares > 0:
    print(f"A soma dos números pares no intervalo é: {soma_pares}")
else:
    print("Portanto, a soma dos números pares é: 0")

print("\n=== Fim do programa ===")