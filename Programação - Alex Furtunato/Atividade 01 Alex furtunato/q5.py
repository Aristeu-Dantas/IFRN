# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostra a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

import random

tupla = tuple(random.randint(0, 1000) 
for i in range(5))
print(tupla)
a=sorted(tupla)
print(f'Maior número: {a[-1]}\nMenor: {a[0]}')
