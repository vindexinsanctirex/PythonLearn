# classe produto, método init com nome, preço e estoque, método mostrar_produto() com nome, quantidade e preço, método valor_total_estoque() que calcule preço x estoque e retorne valor total do estoque daquele produto
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def mostrar_produto(self):
        print(f"Produto: {self.nome} - Preço: R${self.preco:.2f} - Estoque: {self.estoque}")

    def valor_total_estoque(self):
        return self.preco * self.estoque
    
# Criando 3 objetos da classe Produto
produto1 = Produto("Notebook", 3000.00, 10)
produto2 = Produto("Mouse", 100.00, 50)
produto3 = Produto("Teclado", 200.00, 30)

# lista dos produtos criados
produtos = [produto1, produto2, produto3]

# for para percorrer a lista de produtos, mostrar o produto e o valor total do estoque
for produto in produtos:
    produto.mostrar_produto()
    print(f"Valor total do estoque: R${produto.valor_total_estoque():.2f}\n")
    
# variável total_loja começando em 0, usando for para somar o valor total de estoque de todos os produtos, no final do programa, exibir "Valor total do estoque da loja: R$ ..."

total_loja = 0
for produto in produtos:
    total_loja += produto.valor_total_estoque()
    
print(f"Valor total do estoque da loja: R${total_loja:.2f}")