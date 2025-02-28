'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
'''

from time import sleep

lista_composta_notas = []

while True:
  lista_notas = []
  lista_notas.append(input("Nome: ").capitalize())
  lista_notas.append(float(input("Nota 1: ")))
  lista_notas.append(float(input("Nota 2: ")))
  lista_composta_notas.append(lista_notas)

  continua_flag = input("Quer continuar? [S/N] ").strip().upper()[0]

  if continua_flag != 'S':
    break

print("-=" * 30)
print(f"{'ID':<5}{'NOME':<20}{'MÉDIA':<3}")
print("-" * 35)

for pos, lista in enumerate(lista_composta_notas):
  id = pos
  media_aluno = sum(lista[1:]) / 2

  print(f"{id:<5}", end= '')
  print(f"{lista[0]:<20}", end= '')
  print(f"{media_aluno:<3.1f}", end= '')
  print()

print("-" * 35)

while True:
  id_nota = int(input("Mostrar a nota de qual aluno? [ID] (999 Interrompe) "))

  if id_nota == 999:
    print("FINALIZANDO...")
    sleep(2)
    print("Volte Sempre")
    break

  try:
    print(f"Notas de {lista_composta_notas[id_nota][0]}: {lista_composta_notas[id_nota][1:]}")
  except IndexError:
    print(f"Este ID não está atribuído a nenhum aluno.")
  except Exception as e:
    print(type(e))
    print(e)

  print("-" * 35)