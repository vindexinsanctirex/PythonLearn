# Criação do dicionário para armazenar as informações do contato
contato = {}


print("=== Cadastro de Contato ===")


contato['nome'] = input("Digite o nome do contato: ")

contato['telefone'] = input("Digite o número de telefone: ")

contato['email'] = input("Digite o endereço de email: ")

print("\n=== Informações do Contato ===")
print(f"Nome: {contato['nome']}")
print(f"Telefone: {contato['telefone']}")
print(f"Email: {contato['email']}")

print("\n=== Dicionário Completo ===")
print(contato)