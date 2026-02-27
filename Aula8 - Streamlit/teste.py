import os

print("Conteúdo do diretório atual:")
print("-" * 30)

itens = os.listdir('.')
for item in itens:
    print(f"📁 {item}" if os.path.isdir(item) else f"📄 {item}")

print("-" * 30)
print(f"Total: {len(itens)} itens encontrados")