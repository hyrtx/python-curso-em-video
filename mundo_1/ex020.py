'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import shuffle

lista_aluno = []

for i in range(0, 4):
  nome_aluno = input(f"Nome do {i+1}º aluno: ").strip().capitalize()
  lista_aluno.append(nome_aluno)

shuffle(lista_aluno)

print(f"A ordem de apresentação será:\n{lista_aluno}")