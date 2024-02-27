# Faça um programa que recebe um número e calcula o fatorial do mesmo. O programa deve validar o número digitado. 
# Caso o número seja maior que 99, o programa deve informar ao usuário o limite e pedir novamente a digitação.

numerof=int(input('Número a fatorar: '))

resultado=1
count=1
if numerof<=99:
    while numerof>=count:
        resultado*=count
        count+=1
    print(f'Fatorial do número informado é {resultado}')
else:
    print('Número informado não está entre 0 e 99!')