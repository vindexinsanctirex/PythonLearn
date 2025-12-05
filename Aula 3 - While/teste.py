# Número secreto fixo
numero_secreto = 7

# Número máximo de tentativas
max_tentativas = 3

# Contador de tentativas
tentativas = 0

print("=== Jogo de Adivinhação ===")
print(f"Tente adivinhar o número secreto (você tem {max_tentativas} tentativas)!")

# Loop principal do jogo
while tentativas < max_tentativas:
    # Incrementa o contador de tentativas
    tentativas += 1
    
    # Solicita a tentativa do jogador
    try:
        palpite = int(input(f"\nTentativa {tentativas} de {max_tentativas} - Digite um número: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        tentativas -= 1  # Não conta tentativa inválida
        continue
    
    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto}!")
        break  # Sai do loop quando acerta
    
    # Dá uma dica se errou
    elif palpite < numero_secreto:
        print("O número secreto é MAIOR que o seu palpite.")
    else:
        print("O número secreto é MENOR que o seu palpite.")
    
    # Se ainda há tentativas restantes
    if tentativas < max_tentativas:
        print(f"Tente novamente! Você ainda tem {max_tentativas - tentativas} tentativa(s).")
else:
    # Este bloco só é executado se o loop terminar sem o break
    print(f"\nQue pena! Você usou todas as {max_tentativas} tentativas.")
    print(f"O número secreto era {numero_secreto}.")
    print("Não desanime, tente novamente!")

print("\n=== Fim do jogo ===")