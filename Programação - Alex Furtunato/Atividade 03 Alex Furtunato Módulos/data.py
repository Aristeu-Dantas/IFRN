# Faça uma função que recebe os valores de ano, mês e um dia da semana e retorna uma 
# lista com as datas (dias do mês) que caem nesse dia de semana para o mês e ano informados.
# O módulo quando executado deverá solicitar essas informações, executar a função e retornar as datas referentes.

import calendar
ano=0
mes=0
dia=0
dia_semana=0
data=(dia,mes,ano)
data=input('Data: Ex."2/3/2022" ').split('/')
dia=dia_semana
dia_semana=calendar.weekday(ano,mes,dia)
print(dia_semana)
def tempo(dia,mes,ano):
    data=(dia,mes,ano)
    dia_semana=calendar.weekday(dia)
    return print(dia_semana)