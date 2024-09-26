class Aluno:
  def __init__(self, matricula, nome):
    self.m = matricula
    self.n = nome
  def media(self, disciplina, n1, n2):
    self.d = disciplina
    self.media = (n1 * 2 + n2 * 3)/5
  def relatorio(self):
    return f'\n{self.n} tem média {self.media} na disciplina de {self.d}.'
    
aluno1 = Aluno('2020123', 'Vitoria')
aluno2 = Aluno('2020456', 'Guilheme')
aluno3 = Aluno('2020789', 'Kaua')
aluno1.media('Matemática', 8.0, 6.0)
aluno2.media('Banco de Dados', 5.5, 4.0)
aluno3.media('Física', 7.0, 6.0)

print(aluno1.relatorio(), aluno2.relatorio(), aluno3.relatorio())