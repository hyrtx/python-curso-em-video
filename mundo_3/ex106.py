'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o 
comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
'''

def print_titulo(msg: str) -> None:
  print("-=-" * 10)
  print(msg)
  print("-=-" * 10)


def interactive_help() -> None:
  while True:
    print_titulo("SISTEMA DE AJUDA PyHELP")
    funcao = input("Função ou Biblioteca: ")

    if funcao == 'fim':
      print_titulo("Até logo")
      break
    else:
      help(funcao)

interactive_help()