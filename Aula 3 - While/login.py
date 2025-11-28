import getpass

login = "usuario123"
senha = "7010"
tentativas = 0
tentativas_maximas = 5

while tentativas < tentativas_maximas:
    usuario = input("Digite o login do cartão: ")
    entrada = getpass.getpass("Digite a senha do cartão: ")
    if entrada == senha and usuario == login:
        print("Acesso permitido.")
        break
    else:
        tentativas += 1
        print(f"Dados incorretos. Tentativas restantes: {tentativas_maximas - tentativas}")
else:
    print("Conta bloqueada devido a múltiplas tentativas incorretas.")