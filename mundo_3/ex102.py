'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(num: int, show= False) -> None:
  '''
  -> Calcula o fatorial de um número

  :param num: Número a ser calculado
  :param show: (opcional) Mostra ou não o cálculo do fatorial
  :return: O valor do fatorial do argumento num
  '''
  fat = 1
  while num != 0:

    if show == True:
      print(num, end= '')
      if num == 1:
        print(" = ", end= '')
      else:
        print(" x ", end= '')

    fat *= num
    num -= 1
  return fat
    
fatorial(3, show= True)