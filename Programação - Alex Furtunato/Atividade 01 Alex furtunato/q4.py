# Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e último nome separadamente

nome=input('Informe o seu nome completo: ').split()
print(f'Primeiro nome: {nome[0]}\nÚltimo nome: {nome[-1]}')
