from tabulate import tabulate

# informacao = [
#     ["Nome", "Idade", "Cidade"],
#     ["Alice", 30, "São Paulo"],
#     ["Bob", 25, "Rio de Janeiro"],
#     ["Charlie", 35, "Belo Horizonte"]
# ]

# print(tabulate(informacao, headers="firstrow", tablefmt="rounded_outline"))

# menu interativo, adicionar usuários, listar usuários com tabulate, sair, cada usuário deve ser um dicionário com id, nome e email, id não precisa ser passado na função e não pode ser repetido.

usuarios = []

def adicionar_usuario(nome, email):
    id_usuario = len(usuarios) + 1
    usuario = {"id": id_usuario, "nome": nome, "email": email}
    usuarios.append(usuario)
    print(f"Usuário {nome} adicionado com sucesso!")
    
def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return
    print(tabulate(usuarios, headers="keys", tablefmt="fancy_outline"))
    
    
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar usuário")
        print("2. Listar usuários")
        print("3. Remover usuário (opcional)")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = input("Digite o nome do usuário: ")
            email = input("Digite o email do usuário: ")
            if email in [usuario["email"] for usuario in usuarios]:
                print("Email já cadastrado. Tente novamente.")
                continue
            adicionar_usuario(nome, email)
        elif escolha == "2":
            listar_usuarios()
        elif escolha == "3":
            id_remover = int(input("Digite o ID do usuário a remover: "))
            if id_remover in [usuario["id"] for usuario in usuarios]:
                usuarios[:] = [usuario for usuario in usuarios if usuario["id"] != id_remover]
                print(f"Usuário com ID {id_remover} removido (se existia).")
            else:
                print(f"Usuário com ID {id_remover} não encontrado.")
        elif escolha == "4":        
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    menu()