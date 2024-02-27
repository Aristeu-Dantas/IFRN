# Crie um programa onde o usuário possa digitar 10 valores numéricos e cadastre-os em uma lista. 
# Caso o número já esteja lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista=list()
for i in range(10):
    n=input('Adicione um número à lista: ')
    if n in lista:
        print('ja existe')
    else:
        lista.append(n)
print(sorted(lista))