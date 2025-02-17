'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer 
mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

print("-=-" * 20)
print("TERMOS DE UMA PA")
print("-=-" * 20)

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
pa = primeiro_termo
cont = 10
num_termos = 0

while cont > 0:
  print(pa, end=' → ')
  pa += razao
  cont -= 1
  num_termos += 1

  if cont == 0: 
    print("PAUSA")
    cont += int(input("Quantos termos você quer mostrar mais? "))

print(f"Progressão finalizada com {num_termos} termos mostrados")