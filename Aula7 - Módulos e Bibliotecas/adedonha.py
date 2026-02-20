import random

def letra_sorteada():
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letra = random.choice(letras)
    return letra

def adedonha():
    letra = letra_sorteada()
    print(f"A letra sorteada é: {letra}")
    
    # Chama a função de verificação com a letra sorteada
    verificar_respostas(letra)

def verificar_respostas(letra):
    # Solicita as respostas do usuário
    nome = input("Digite um nome: ").upper()  # Converte para maiúsculas
    lugar = input("Digite um lugar: ").upper()
    animal = input("Digite um animal: ").upper()
    cor = input("Digite uma cor: ").upper()
    
    # Verifica se todas começam com a letra sorteada
    if (nome.startswith(letra) and lugar.startswith(letra) and 
        animal.startswith(letra) and cor.startswith(letra)):
        print("Parabéns! Todas as respostas estão corretas!")
        
        # Mostra as respostas
        print(f"\nSuas respostas:")
        print(f"Nome: {nome}")
        print(f"Lugar: {lugar}")
        print(f"Animal: {animal}")
        print(f"Cor: {cor}")
    else:
        print("Alguma resposta está incorreta. Tente novamente.")
        
        # Mostra quais estão erradas (opcional - feedback adicional)
        if not nome.startswith(letra):
            print(f"❌ Nome '{nome}' não começa com {letra}")
        if not lugar.startswith(letra):
            print(f"❌ Lugar '{lugar}' não começa com {letra}")
        if not animal.startswith(letra):
            print(f"❌ Animal '{animal}' não começa com {letra}")
        if not cor.startswith(letra):
            print(f"❌ Cor '{cor}' não começa com {letra}")

if __name__ == "__main__":
    adedonha()