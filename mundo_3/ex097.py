'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.
'''

def print_especial(mensagem: str) -> None:
  tamanho_frame = len(mensagem) + 4

  print("~" * tamanho_frame)
  print(f"  {mensagem}")
  print("~" * tamanho_frame)

print_especial("Curso em Vídeo: Python")