class Aluno:
    def __init__(self, nome):
        self.__nome = nome

class Turma:
    def __init__(self, nome):
        self.__nome = nome
        self.__alunos = []

    def adicionar_aluno(self, objeto_aluno):
        if isinstance(objeto_aluno, Aluno):
            self.__alunos.append(objeto_aluno)
        else:
            print("Erro: O objeto não é uma instância da classe Aluno.")
            
# Criando instâncias de Aluno
aluno1 = Aluno("João")
aluno2 = Aluno("Maria")
aluno3 = Aluno("Pedro")
aluno4 = Aluno("Ana")

turma_a = Turma("Turma A")

turma_a.adicionar_aluno(aluno1)
turma_a.adicionar_aluno(aluno2)
