def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc <= 0:
        return "IMC inválido"
    else:
        return round(imc, 2)
    
    
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"
    
