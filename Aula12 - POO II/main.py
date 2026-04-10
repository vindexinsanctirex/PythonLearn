class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.__nome}")

class Professor(Pessoa):
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu ensino aqui.")

class Aluno(Pessoa):
    def __init__(self, nome, nota):
        super().__init__(nome)
        self.__nota = nota

        if nota >= 7:
            self.__status = 'Aprovado'
        else:
            self.__status = 'Reprovado'
            
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu estudo aqui.")
    
    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def set_nota(self, nova_nota):
        if nova_nota >= 0 and nova_nota <= 10:
            self.__nota = nova_nota
        else:
            raise ValueError("A nota precisa estar entre 0 e 10!")

class Disciplina:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class Turma:
    def __init__(self, turma):
        self.__turma = turma
        self.__alunos = []
        self.__disciplinas = []

    @property
    def alunos(self):
        if self.__alunos:
            for i in self.__alunos:
               print(i.nome)
        else:
            print("Não há alunos nessa turma!")

    def adicionar_aluno(self, objeto_aluno):
        if isinstance(objeto_aluno, Aluno):
            self.__alunos.append(objeto_aluno)
        else:
            raise ValueError("Precisa ser um objeto instanciado da classe Aluno!")
        
aluno_1 = Aluno("Aline", 10)
pessoa_1 = Pessoa("Pedro")
professor_1 = Professor("Maria")

aluno_1.apresentar()
pessoa_1.apresentar()
professor_1.apresentar()