'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

from datetime import datetime
from calendar import isleap

ano = int(input("Qual ano você quer analisar? Digite 0 para analisar o ano atual. "))

if ano == 0:
  ano = datetime.today().year

if isleap(ano):
  print(f"O ano {ano} é BISSEXTO!")
else:
  print(f"O ano {ano} NÃO É BISSEXTO!")