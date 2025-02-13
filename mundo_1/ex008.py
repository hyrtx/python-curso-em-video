'''
Escreva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, dm, cm e mm.
'''

distancia_metros = float(input("Digite uma distaância em metros: "))

print(f"A medida de {distancia_metros} corresponde a: ")
print(f"{distancia_metros / 1000}km")
print(f"{distancia_metros / 100}hec")
print(f"{distancia_metros / 10}dam")
print(f"{distancia_metros * 10}dm")
print(f"{distancia_metros * 100}cm")
print(f"{distancia_metros * 1000}mm")