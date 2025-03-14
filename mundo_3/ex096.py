'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(lar: float, comp: float) -> float:
  area = lar * comp
  return area

print("Controle de Terrenos")
print("-" * 20)

largura = float(input("LARGURA (m): "))
comprimento = float(input("COMPRIMENTO (m): "))
area = area(largura, comprimento)

print(f"A área de um terreno {largura:.1f}x{comprimento:.1f} é de {area:.1f}m²")