import funcoes_matematicas as fm

def delta():
    numeros = 5, 6, 7
    delta = fm.calcular_delta(*numeros)
    print(f"O delta de {numeros} é: {delta}")
    
def raizes():
    numeros = 1, -5, 6
    raizes = fm.calcular_raizes(*numeros)
    print(f"As raízes de {numeros} são: {raizes}")
    
if __name__ == "__main__":
    raizes()
    delta()

