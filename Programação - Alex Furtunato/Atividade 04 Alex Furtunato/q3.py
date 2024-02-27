# Faça um programa que receba uma lista de números inteiros separados por ":" e deve armazená-los numa lista.
# A lista deve ser ordenada em ordem crescente e os números digitados devem ser inteiros.
# caso haja algum item digitado que não seja um número inteiro, o mesmo deve ser ignorado e não adicionado à lista.

inteiros=input("Informe a lista de número separados por ':' : ").split(':')
lista=[]

for i in inteiros(1):
    cont=inteiros.count(i)
    if cont>1:
        lista.append(i-(cont-1))
    else:
        lista.append(i)

print(sorted(lista))