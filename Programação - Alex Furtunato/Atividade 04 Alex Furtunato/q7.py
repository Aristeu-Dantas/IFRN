# Crie um programa que simule um caixa eletrônico. Você digita o valor que quer sacar e ele diz 
# quantas cédulas ele vai entregar. Suponha que o caixa tem cédulas de 50, 20, 10, 5 e 1 real.

saque=int(input('Informe o valor que quer sacar: '))

#CONSTRUTORES
total=saque
ced=50
totalced=0

#CALCULANDO
while True:
    if total>=ced:
        total-=ced
        totalced+=1
    else:
        if totalced>0:
            print('O total de {0} cédulas de R${1}'.format(totalced,ced))
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=5
        elif ced==5:
            ced=1
        totalced=0
        if total==0:
            break