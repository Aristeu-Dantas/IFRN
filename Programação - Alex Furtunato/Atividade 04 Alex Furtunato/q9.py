# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida em uma lista. 
# No final, tudo isso será guardado em um dicionário. 
# O programa deverá imprimir o relatório com as informações colhidas e 
# o aproveitamento do jogador como o número médio de gols por partida.

jogador = dict()

#Recebendo e organizando informações
jogador['nome'] = input('Nome do jogador: ').strip().capitalize()

qtd_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
print()

jogador['gols'] = []  # Adicionando lista de gols na ficha do jogador
total_gols = 0

# Adicionando gols
for partida in range(qtd_partidas):
    jogador['gols'].append(int(input(f'\tGols da {partida + 1}º partida: ')))
    total_gols += jogador['gols'][partida]

# Adicionando o total de gols feitos na ficha do jogador
jogador['total'] = total_gols

# Dicionário completo
print('*' * 60)
print(jogador)
print('*' * 60)

# Campos e seus dados
for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}.')
print()

# Mostrando gols por partida
print(f'O jogador {jogador["nome"]} jogou {qtd_partidas} partidas.')
for partida, gol in enumerate(jogador['gols']):
    print(f'\t--> Na {partida + 1}º, fez {gol} gols.')
print(f'Foi um total de {jogador["total"]}')