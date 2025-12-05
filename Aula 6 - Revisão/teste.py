# Versão mais compacta
print("=== SISTEMA DE LOGIN ===")

# Credenciais fixas
USER = "admin"
PASS = "1234"

# Loop de tentativas
for tentativa in range(3, 0, -1):  # 3, 2, 1
    print(f"\nTentativas restantes: {tentativa}")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario == USER and senha == PASS:
        print("\n✅ Acesso concedido! Bem-vindo!")
        break
    else:
        print("❌ Credenciais incorretas!")
else:
    # Este bloco else executa apenas se o loop NÃO foi interrompido por break
    print("\n" + "="*30)
    print("ACESSO BLOQUEADO!")
    print("="*30)
    
    # Loop for para exibir a mensagem 3 vezes
    for _ in range(3):
        print("ACESSO BLOQUEADO")
    
    print("Contate o administrador do sistema.")

print("\nFim do programa.")