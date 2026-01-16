#mini sistema bancário, com as seguintes funcionalidades:
#- criar conta
#- depositar
#- sacar
#- mostrar saldo
# cada conta deve ser representada por um dicionário com nome do titular e saldo

def criar_conta(titular, saldo_inicial=0):
    return {"titular": titular, "saldo": saldo_inicial}

def depositar(conta, valor):
    if valor > 0:
        conta["saldo"] += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("Valor de depósito inválido.")
        
def sacar(conta, valor):
    if 0 < valor <= conta["saldo"]:
        conta["saldo"] -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
    else:
        print("Saldo insuficiente ou valor inválido.")
        
def mostrar_saldo(conta):
    print(f"Saldo atual de {conta['titular']}: R${conta['saldo']:.2f}")
    
def transferir(conta_origem, conta_destino, valor):
    if 0 < valor <= conta_origem["saldo"]:
        conta_origem["saldo"] -= valor
        conta_destino["saldo"] += valor
        print(f"Transferência de R${valor:.2f} realizada com sucesso.")
    else:
        print("Saldo insuficiente ou valor inválido.")
        
def listar_contas(contas):
    for conta in contas:
        print(f"Titular: {conta['titular']}, Saldo: R${conta['saldo']:.2f}")
    
múltiplas_contas = []

conta1 = criar_conta("Alice", 1000)
múltiplas_contas.append(conta1)
conta2 = criar_conta("Bob", 500)
múltiplas_contas.append(conta2)
conta3 = criar_conta("Charlie")
múltiplas_contas.append(conta3)
conta4 = criar_conta("Diana", 750)
múltiplas_contas.append(conta4)
conta5 = criar_conta("Ethan", 300)
múltiplas_contas.append(conta5)

def selecionar_opcao():
    print("\nOpções:")
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Mostrar saldo")
    print("5. Transferir")
    print("6. Listar todas as contas")
    print("7. Sair")
    return input("Escolha uma opção (1-7): ")

while True:
    opcao = selecionar_opcao()
    
    if opcao == "1":
        nome = input("Digite o nome do titular: ")
        saldo_inicial = float(input("Digite o saldo inicial (ou 0 para nenhum): "))
        nova_conta = criar_conta(nome, saldo_inicial)
        múltiplas_contas.append(nova_conta)
        print(f"Conta criada para {nome} com saldo inicial de R${saldo_inicial:.2f}.")
        
    elif opcao == "2":
        nome = input("Digite o nome do titular da conta para depósito: ")
        conta_encontrada = next((conta for conta in múltiplas_contas if conta["titular"] == nome), None)
        if conta_encontrada:
            valor = float(input("Digite o valor a depositar: "))
            depositar(conta_encontrada, valor)
        else:
            print("Conta não encontrada.")
            
    elif opcao == "3":
        nome = input("Digite o nome do titular da conta para saque: ")
        conta_encontrada = next((conta for conta in múltiplas_contas if conta["titular"] == nome), None)
        if conta_encontrada:
            valor = float(input("Digite o valor a sacar: "))
            sacar(conta_encontrada, valor)
        else:
            print("Conta não encontrada.")
            
    elif opcao == "4":
        nome = input("Digite o nome do titular da conta para mostrar saldo: ")
        conta_encontrada = next((conta for conta in múltiplas_contas if conta["titular"] == nome), None)
        if conta_encontrada:
            mostrar_saldo(conta_encontrada)
        else:
            print("Conta não encontrada.")
            
    elif opcao == "5":
        nome_origem = input("Digite o nome do titular da conta de origem: ")
        nome_destino = input("Digite o nome do titular da conta de destino: ")
        conta_origem = next((conta for conta in múltiplas_contas if conta["titular"] == nome_origem), None)
        conta_destino = next((conta for conta in múltiplas_contas if conta["titular"] == nome_destino), None)
        if conta_origem and conta_destino:
            valor = float(input("Digite o valor a transferir: "))
            transferir(conta_origem, conta_destino, valor)
        else:
            print("Conta de origem ou destino não encontrada.")
            
    elif opcao == "6":
        listar_contas(múltiplas_contas)
        
    elif opcao == "7":
        print("Saindo do sistema bancário. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")