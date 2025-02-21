'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

tupla_palavras = ('aprender', 'programar', 'linguagem', 'python',
                  'curso', 'gratis', 'estudar', 'praticar',
                  'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in tupla_palavras:
  print(f"Na palavra {palavra.upper()} nós temos: ", end= '')

  for letra in palavra:
    if letra in 'aeiou':
      print(letra, end= ' ')
      
  print("")