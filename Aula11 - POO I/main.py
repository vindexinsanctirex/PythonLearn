# classe Aluno, dentro da classe método construtor parqa receber nome, nota1 e nota2, atribuindo ao self, método calcular_media() e método verificar_status() que mostre "Aprovado" se for >= 7, "Reprovado" caso contrário

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def verificar_status(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"