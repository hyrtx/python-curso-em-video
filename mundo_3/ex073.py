'''
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela 
do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

1. Os 5 primeiros times.
2. Os últimos 4 colocados.
3. Times em ordem alfabética.
4. Em que posição está o time do Flamengo.

PS.: Tabela Brasileirão 2024.
'''

colocacao_times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional',
                   'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco',
                   'Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude',
                   'Bragantino', 'Atlético-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

print("-=-" * 10)
print("INFORMATIVO BRASILEIRÃO 2024")
print("-=-" * 10)

print(f"Os cinco primeiros times são: {colocacao_times[:5]}\n")
print(f"Os quatro últimos times são: {colocacao_times[-4:]}\n")
print(f"Time em ordem alfabética: {sorted(colocacao_times)}\n")
print(f"A colocação do Flamengo foi: {colocacao_times.index('Flamengo') + 1}º lugar")