# Crie uma programa que recebe do usuário a lista de nomes de times (20 times) em ordem de classificação no
# campeonato brasileiro e os armazena(na mesma ordem) em um tupla. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Ceará.

lista_times = tuple()
lista_times = str(input('Informe a lista de times: ')).split()


# Letra A
a = lista_times[0:5]
print(a)

#Letra B
b= lista_times[15:19]
print(b)

#Letra C
convert=list(lista_times)
c = sorted(lista_times)
print(c)

#Letra D
d=lista_times.index('Ceará')
print(d)