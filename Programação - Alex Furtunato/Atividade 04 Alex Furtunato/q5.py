# Faça um programa que espere a digitação de duas datas no formato "dd/mm/aaaa" e calcule a quantidade de dias entre as duas datas.

usuariodata1=input('Informe a primeira data no formato "dd/mm/aaaa": ')
usuariodata2=input('Informe a primeira data no formato "dd/mm/aaaa": ')

Datas=usuariodata1.split("/")
Datas1=[int(Datando) for Datando in Datas]

Dia, Mes, Ano = Datas1

MES = Mes-1
NumerosdeDias=0
Contador=1 

while Contador < MES:
    if Contador in (3,5,7,8,10,12):
        NumerosdeDias+=31
    elif Contador in (4,6,9,11):
        NumerosdeDias+=30
    else:
        NumerosdeDias+=28
    Contador+=1

Verifique=(365- NumerosdeDias - Dia - 1)

Datas2=usuariodata2.split("/")
Datas3=[int(Datador) for Datador in Datas2]

Dia1, Mes1, Ano1= Datas3

ANO= Ano1-1
MES1 = Mes1-1
NumeroDeDias=0 
Contadores=1 

while Contadores <= MES1:
  if Contadores in (4,6,9,11):
    NumeroDeDias+=30
  elif Contadores in (1,3,5,7,8,10):
    NumeroDeDias+=31
  else:
    NumeroDeDias+=28
  Contadores+=1
Verificador = (365- NumeroDeDias - Dia1 - 23)

AnoFinal=(Ano1-Ano)
AnoFinal2=AnoFinal*365

if Ano%4 ==0:
  if Mes==2 and Dia==28:
    bissexto=(Ano1-Ano)//4
  else:
    bissexto=(Ano1-Ano)//4-1
elif Ano%4==0:
  if Mes1 ==2:
     bissexto=(Ano1-Ano)//4
  else:
    bissexto=(Ano1-Ano)//4-1
else:
  bissexto=(Ano1-Ano)//4

Verificando = AnoFinal2-bissexto
print(Verifique+Verificador +Verificando)
