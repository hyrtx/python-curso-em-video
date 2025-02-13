'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''

from random import choice

lista_aluno = []

for i in range(0, 4):
  nome_aluno = input(f"Nome do {i+1}º aluno: ").strip().capitalize()
  lista_aluno.append(nome_aluno)

aluno_sorteado = choice(lista_aluno)

print(f"O aluno(a) escolhido foi {aluno_sorteado}")