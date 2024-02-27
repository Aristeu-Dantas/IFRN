# Escreva um programa para ler o número total de eleitores de um município, 
# o número de votos brancos e o número de votos nulos. 
# Considerando que todos os eleitores compareceram à votação, 
# o programa deve calcular o percentual dos votos apurados (válidos, brancos e nulos).

total_eleitores=int(input('Informe o número total de eleitores: '))
nulo=int(input('Informe quantos votos nulos tiveram: '))
branco=int(input('Informe quantos votos em branco tiveram: '))

if nulo>total_eleitores or branco>total_eleitores:
    print('Algo deu errado. Tente novamente...')
else:
    percentual_nulo=nulo/total_eleitores
    percentual_branco=branco/total_eleitores
    votos_validos=total_eleitores-(percentual_branco+percentual_nulo)
    print(f'O percentual de votos brancos é {percentual_branco}%.\nJá o percentual de votos nulos é {percentual_nulo}%.\nVotos válidos {votos_validos}.')
