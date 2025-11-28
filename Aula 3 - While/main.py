# # imprimir tabuada de número recebido em input
# num = int(input("Digite um número para ver sua tabuada: "))
# print(f"Tabuada de {num}:")
# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num * i}")
#     i += 1
    
# i = 0

# while i < 10:
#     i+= 1
#     if i % 2 != 0:
#         continue
#     print(i)
    
while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print(f"Nota {int(nota)} registrada com sucesso.")
        break
    else:
        print("Nota inválida. Tente novamente.")
        
