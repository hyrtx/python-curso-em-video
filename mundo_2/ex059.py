'''
Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

print("[ 1 ] somar")
print("[ 2 ] multiplicar")
print("[ 3 ] maior")
print("[ 4 ] novos números")
print("[ 5 ] sair do programa")

while True:
  escolha = int(input("Qual é a sua opção: "))

  if not 1 <= escolha <= 5:
    print("Opção inválida, tente novamente.")

  elif escolha == 1:
    print(f"{primeiro_valor} + {segundo_valor} = {primeiro_valor + segundo_valor}")
    print("-=-" * 25)

  elif escolha == 2:
    print(f"{primeiro_valor} x {segundo_valor} = {primeiro_valor * segundo_valor}")
    print("-=-" * 25)

  elif escolha == 3:
    print(f"O maior valor entre {primeiro_valor} e {segundo_valor} é: {max(primeiro_valor, segundo_valor)}")
    print("-=-" * 25)

  elif escolha == 4:
    primeiro_valor = int(input("Digite o primeiro valor: "))
    segundo_valor = int(input("Digite o segundo valor: "))
    continue

  else:
    print("Finalizando...")
    sleep(2)
    print("Programa finalizado")
    break