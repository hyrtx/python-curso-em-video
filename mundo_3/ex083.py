'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expressao = input("Digite a expressão: ")

parenteses_abertos = expressao.count('(')
parenteses_fechados = expressao.count(')')

if parenteses_abertos == parenteses_fechados:
  print("Sua expressão está correta!")
else:
  print("Sua expressão está errada!")