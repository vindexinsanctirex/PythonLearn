from datetime import datetime

# registrar horário de saída do laboratório ao apertar o botão ENTER, calculando o tempo de estadia com registrar o tempo de entrada que deve ser considerado quando aplicado a função
def registrar_horario():
    horario_entrada = datetime.now()
    print(f"Horário de entrada registrado: {horario_entrada.strftime('%H:%M:%S')}")
    
    input("Pressione ENTER para registrar o horário de saída...")
    
    horario_saida = datetime.now()
    print(f"Horário de saída registrado: {horario_saida.strftime('%H:%M:%S')}")
    
    tempo_estadia = horario_saida - horario_entrada
    print(f"Tempo de estadia: {tempo_estadia}")
    
if __name__ == "__main__":
    registrar_horario()