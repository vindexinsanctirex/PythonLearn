# Classe Animal independente
class Animal:
    def falar(self):
        print("Este animal faz um som genérico.")

# Classe Cachorro independente
class Cachorro:
    def falar(self):
        print("O cachorro está latindo.")

# Classe Gato independente
class Gato:
    def falar(self):
        print("O gato está miando.")

# Criando objetos e chamando o método falar()
animal = Animal()
cachorro = Cachorro()
gato = Gato()

# Chamando o método falar() de cada objeto
animal.falar()
cachorro.falar()
gato.falar()