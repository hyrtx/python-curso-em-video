'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema 
de visualização de detalhes do aproveitamento de cada jogador.
'''

# Funções
def continua_programa():
  while True:
    flag_continua = input("Quer continuar? [S/N] ").strip().upper()[0]

    if flag_continua in 'SN':
      return flag_continua
    else:
      print("ERRO! Escolha 'S' para sim ou 'N' para não.")

def mostrar_dados_jogador():
  while True:
    try:
      flag_mostrar_dado_jogador = int(input("Mostrar dado de qual jogador? [Digite ID, 999 para parar] "))
      return flag_mostrar_dado_jogador
    except TypeError:
      print("ERRO! Digite um valor numérico")
    except Exception as e:
      print(e)
      print(type(e))

# Variáveis de armazenamento
lista_jogadores = list()
registro_jogadores = dict()
lista_gols = list()

# Inicio programa
while True:
  registro_jogadores = {
      'nome': input("Nome do] jogador: ").strip().title(),
      'partidas': int(input(f"Número de partidas: ")),
      'gols': list()
  }

  for g in range(registro_jogadores['partidas']):
    gols = int(input(f" → Gols na {g + 1}ª partida: "))
    registro_jogadores['gols'].append(gols)

  registro_jogadores['total_gols'] = sum(registro_jogadores['gols'])

  lista_jogadores.append(registro_jogadores)

  if continua_programa() == 'N':
    break

print("-=-" * 18)
print(f"{'cod':<5}{'nome':<15}{'gols':<30}{'total':<5}")
print("-" * 55)

for p, v in enumerate(lista_jogadores):
  print(f"{p:<5}{v['nome']:<15}{str(v['gols']):<30}{v['total_gols']:<5}")
print("-" * 55)

while True:
  id_escolha = mostrar_dados_jogador()

  if id_escolha == 999:
    print("ENCERRADO")
    break
  elif not 0 <= id_escolha < len(lista_jogadores):
    print("Esse ID não existe")
  else:
    print(f"--- Levantamento de dados do jogador {lista_jogadores[id_escolha]['nome']}")
    for p, v in enumerate(lista_jogadores[id_escolha]['gols'], start= 1):
      print(f"    No jogo {p} fez {v} gols.")
    print("-" * 55)