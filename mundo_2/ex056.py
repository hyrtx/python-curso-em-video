'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e 
quantas mulheres têm menos de 20 anos.
'''

pessoas_list = []

for x in range(0, 4):
  pessoas_dict = {}
  print(f"----- {x+1}ª PESSOA -----")
  pessoas_dict['nome'] = input("Nome: ").strip().capitalize()
  pessoas_dict['idade'] = int(input("Idade: "))
  pessoas_dict['sexo'] = input("Sexo [M/F]: ").strip().upper()
  pessoas_list.append(pessoas_dict)

homem_mais_velho = max(
    (p for p in pessoas_list if p['sexo'] == 'M'),
    key= lambda p: p['idade'],
    default= None)

media_grupo = sum(p["idade"] for p in pessoas_list) / len(pessoas_list)
mulheres_menos_20 = sum(1 for p in pessoas_list if p['sexo'] == 'F' and p['idade'] < 20)

print(f"A media de idade do grupo é de {media_grupo} anos.")
print(f"Ao todo são {mulheres_menos_20} mulheres com menos de 20 anos")
print(f"O nome do homem mais velho é {homem_mais_velho['nome']}, e ele tem {homem_mais_velho['idade']} anos.")