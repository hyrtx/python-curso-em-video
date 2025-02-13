'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

primeira_nota = float(input("Digite a primeira nota do aluno: "))
segunda_nota = float(input("Digite a segunda nota do aluno: "))

media = (primeira_nota + segunda_nota) / 2

print(f"A média entre {primeira_nota} e {segunda_nota} é igual a {media}")