'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes
'''

print("-=-" * 20)
print("Analisador de triângulos")
print("-=-" * 20)

primeiro_segmento = float(input("Digite o primeiro segmento: "))
segundo_segmento = float(input("Digite o segundo segmento: "))
terceiro_segmento = float(input("Digite o terceiro segmento: "))

if primeiro_segmento == segundo_segmento == terceiro_segmento:
  print("Os segmentos acima podem formar um triângulo EQUILÁTERO!")
elif primeiro_segmento == segundo_segmento or segundo_segmento == terceiro_segmento or terceiro_segmento == primeiro_segmento:
  print("Os segmentos acima podem formar um triângulo ISÓSCELES!")
elif primeiro_segmento != segundo_segmento != terceiro_segmento:
  print("Os segmentos acima podem formar um triângulo ESCALENO!")
