# Escreva um programa que encontre as raízes da equação abaixo. 
# Os valores de A, B e C deverão ser solicitados ao usuário:

# Ax2+Bx+ C=0
from math import sqrt

a=float(input('Informe o valor de "A": '))
b=float(input('Informe o valor de "B": '))
c=float(input('Informe o valor de "c": '))

x1= (-b + sqrt(b**2-4*a*c))/(2*a)
x2= (-b - sqrt(b**2-4*a*c))/(2*a)

print(f'Valor de x1: {x1}\nValor de x2: {x2}')
