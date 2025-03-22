'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai 
retornar um dicionário com as seguintes informações:

Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''

def notas(*notas: float, sit: bool = False) -> dict:
  '''
  Função para analisar as notas dos alunos e gerar um panorama da situação da turma

  Parâmetros
  ----------
  notas: (Múltiplas) Recebe as notas da turma, sem limite de quantidade
  sit:   (Opcional) Indica se deve imprimir ou não a situação da turma

  Retorno
  -------
  Dicionário com:
   - Quantidade de notas
   - Maior nota entre a turma
   - Menor nota entre a turma
   - Média das notas da turma
   - Situação da turma, onde: (Se sit = False)
     * Média das notas da turma < 5 = RUIM
     * Média das notas da turma < 7 = REGULAR
     * Média das notas da turma < 9 = BOM
     * Média das notas da turma >= 9 = EXCELENTE
  '''
  arquivo = dict()

  arquivo['qtd_notas'] = len(notas)
  arquivo['maior_nota'] = max(notas)
  arquivo['menor_nota'] = min(notas)
  arquivo['media_turma'] = round(sum(notas) / arquivo['qtd_notas'], 2)

  if sit:
    if arquivo['media_turma'] < 5:
      arquivo['situacao'] = 'RUIM'
    elif arquivo['media_turma'] < 7:
      arquivo['situacao'] = 'REGULAR'
    elif arquivo['media_turma'] < 9:
      arquivo['situacao'] = 'BOM'
    else:
      arquivo['situacao'] = 'EXCELENTE'

  return arquivo

notas(9, 10, 8.7, sit= True)
help(notas)