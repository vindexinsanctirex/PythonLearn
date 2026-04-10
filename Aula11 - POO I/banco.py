# classe ContaBancaria, método init com nome do titular e saldo, método depositar() para adicionar valor ao saldo, método sacar() para subtrair valor do saldo, método mostrar_saldo() para exibir o saldo atual
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente para saque.")
    
    def mostrar_saldo(self):
        print(f"Saldo de {self.titular}: R$ {self.saldo:.2f}")
        
# Criando 3 objetos da classe ContaBancaria
conta1 = ContaBancaria("Alice", 1000)
conta2 = ContaBancaria("Bob", 500)
conta3 = ContaBancaria("Charlie", 200)

# lista das contas criadas
contas = [conta1, conta2, conta3]

# usar o programa para depositar, sacar e mostrar saldo de cada conta
conta1.depositar(500)
conta2.sacar(200)
conta3.depositar(300)
conta1.mostrar_saldo()
conta2.mostrar_saldo()
conta3.mostrar_saldo()