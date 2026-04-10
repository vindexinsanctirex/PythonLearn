class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")

class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")

class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")

# Instanciando os objetos
veiculo = Veiculo()
carro = Carro()
moto = Moto()

# Demonstrando o funcionamento
print("Demonstração do polimorfismo:")
print("-" * 30)

print("Chamando movimentar() do Veiculo:")
veiculo.movimentar()

print("\nChamando movimentar() do Carro:")
carro.movimentar()

print("\nChamando movimentar() da Moto:")
moto.movimentar()