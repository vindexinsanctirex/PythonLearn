print("=== Sistema de Cálculo de Médias da Turma ===")
print("")

# Solicita o número de alunos
try:
    num_alunos = int(input("Digite o número de alunos na turma: "))
    if num_alunos <= 0:
        print("Número de alunos deve ser maior que zero!")
        exit()
except ValueError:
    print("Erro: Digite um número inteiro válido!")
    exit()

# Listas para armazenar os dados
nomes_alunos = []
medias_alunos = []
todas_notas = []  # Para calcular a média geral
aprovados = 0
reprovados = 0

print("\n" + "="*60)
print(f"Vamos coletar os dados dos {num_alunos} aluno(s):")
print("="*60)

# Loop para cada aluno
for i in range(num_alunos):
    print(f"\n--- Aluno {i+1} de {num_alunos} ---")
    
    # Solicita o nome do aluno
    nome = input(f"Digite o nome do aluno {i+1}: ").strip()
    while not nome:
        nome = input("Nome inválido! Digite o nome do aluno: ").strip()
    
    notas = []
    
    # Loop para as 3 notas
    for j in range(3):
        while True:
            try:
                nota = float(input(f"  Digite a {j+1}ª nota (0-10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("  Nota inválida! Digite um valor entre 0 e 10.")
            except ValueError:
                print("  Erro! Digite um número válido.")
    
    # Calcula a média do aluno
    media_aluno = sum(notas) / len(notas)
    
    # Verifica aprovação
    situacao = "APROVADO" if media_aluno >= 7.0 else "REPROVADO"
    
    # Atualiza contadores
    if media_aluno >= 7.0:
        aprovados += 1
    else:
        reprovados += 1
    
    # Armazena os dados
    nomes_alunos.append(nome)
    medias_alunos.append(media_aluno)
    todas_notas.extend(notas)
    
    # Exibe os dados do aluno
    print(f"\n  RESUMO DO ALUNO:")
    print(f"  Nome: {nome}")
    print(f"  Notas: {notas[0]:.1f}, {notas[1]:.1f}, {notas[2]:.1f}")
    print(f"  Média: {media_aluno:.1f}")
    print(f"  Situação: {situacao}")
    
    # Linha separadora
    if i < num_alunos - 1:
        print("-"*40)

print("\n" + "="*60)
print("RELATÓRIO FINAL DA TURMA")
print("="*60)

# Exibe resultado de cada aluno
print("\nDESEMPENHO INDIVIDUAL:")
for i in range(num_alunos):
    situacao = "APROVADO" if medias_alunos[i] >= 7.0 else "REPROVADO"
    print(f"{i+1:2d}. {nomes_alunos[i]:15s} | Notas: {'/'.join([f'{n:.1f}' for n in todas_notas[i*3:i*3+3]])} | Média: {medias_alunos[i]:5.1f} | {situacao}")

# Calcula e exibe a média geral
if todas_notas:
    media_geral = sum(todas_notas) / len(todas_notas)
else:
    media_geral = 0

print("\n" + "="*60)
print("ESTATÍSTICAS DA TURMA:")
print("="*60)
print(f"Total de alunos: {num_alunos}")
print(f"Aprovados: {aprovados} ({aprovados/num_alunos*100:.1f}%)")
print(f"Reprovados: {reprovados} ({reprovados/num_alunos*100:.1f}%)")
print(f"Média geral da turma: {media_geral:.2f}")

print("\n=== Fim do programa ===")