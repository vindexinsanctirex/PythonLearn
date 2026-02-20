import random

def lancar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    
    soma = dado1 + dado2
    
    return soma

# Exemplo de uso:
if __name__ == "__main__":
    resultado = lancar_dados()
    print(f"A soma dos dados é: {resultado}")