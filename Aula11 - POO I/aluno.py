from main import Aluno

# Criando um objeto da classe Aluno
aluno1 = Aluno("João", 8.5, 7.0)
aluno2 = Aluno("Maria", 6.0, 5.5)
aluno3 = Aluno("Pedro", 9.0, 8.5)

# Verificando o status de cada aluno
print(f"{aluno1.nome} - Média: {aluno1.calcular_media():.2f} - Status: {aluno1.verificar_status()}")
print(f"{aluno2.nome} - Média: {aluno2.calcular_media():.2f} - Status: {aluno2.verificar_status()}")
print(f"{aluno3.nome} - Média: {aluno3.calcular_media():.2f} - Status: {aluno3.verificar_status()}")